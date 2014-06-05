
'''
MAP Client Plugin Step
'''
import os

from PySide import QtGui
from PySide import QtCore

from mountpoints.workflowstep import WorkflowStepMountPoint
from fieldworkpcmeshfittingstep.configuredialog import ConfigureDialog
from fieldworkpcmeshfittingstep.mayavipcmeshfittingviewerwidget import MayaviPCMeshFittingViewerWidget

import copy
from fieldwork.field import geometric_field_fitter as GFF
from gias.learning import PCA_fitting
from mappluginutils.datatypes import transformations
import numpy as np

class FieldworkPCMeshFittingStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    _distModes = ('DPEP', 'EPDP')

    _configDefaults = {}
    _configDefaults['identifier'] = ''
    _configDefaults['Distance Mode'] = 'EPDP'
    _configDefaults['PCs to Fit'] = '4'
    _configDefaults['Surface Discretisation'] = '10'
    _configDefaults['Mahalanobis Weight'] = '0.1'
    _configDefaults['Max Func Evaluations'] = '1000'
    _configDefaults['xtol'] = '1e-6'
    _configDefaults['Fit Scale'] = 'False'
    _configDefaults['N Closest Points'] = '1'
    _configDefaults['GUI'] = 'True'

    def __init__(self, location):
        super(FieldworkPCMeshFittingStep, self).__init__('Fieldwork PC Mesh Fitting', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Fitting'
        # Add any other initialisation code here:
        # Ports:
        # data cloud (2d numpy array)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#pointcoordinates'))

        # GF to fit (geometric_field)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))

        # principal components (gias.learning.PCA.PrincipalComponents)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#principalcomponents'))

        # initial transform (transform class)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#geometrictransform'))

        # data weights (1d numpy array, optional)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'numpyarray1d'))

        # fitted GF (geometric_field)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodel'))

        # fitted params (rigid + mode scores)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#geometrictransform'))

        # RMS error (float)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'float'))

        # error for each data point (1d numpy array)
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'numpyarray1d'))

        self._config = {}
        for k, v in self._configDefaults.items():
            self._config[k] = v

        self._pc = None
        self._data = None
        self._dataWeights = None
        self._GFUnfitted = None
        self._GF = None
        self._GFFitted = None
        self._RMSEFitted = None
        self._T0 = None
        self._TFitted = None
        self._fitErrors = None
        self._fitter = None

        self._widget = None

    def _fit(self):

        # parse parameters
        if self._config['Distance Mode']=='DPEP':
            objMaker = GFF.makeObjDPEP
        elif self._config['Distance Mode']=='EPDP':
            objMaker = GFF.makeObjEPDP
        fitModes = range(1, int(self._config['PCs to Fit']))
        GD = [int(self._config['Surface Discretisation']),]*2
        mWeight = float(self._config['Mahalanobis Weight'])
        xtol = float(self._config['xtol'])
        fitScale = self._config['Fit Scale']
        nClosestPoints = int(self._config['N Closest Points'])
        reqNParams = 6 + len(fitModes) + 1
        if fitScale:
            reqNParams += 1

        # initialise fitter
        PCFitter = PCA_fitting.PCFit()
        PCFitter.setPC(self._pc)
        PCFitter.xtol = xtol
        segElements = self._GF.ensemble_field_function.mesh.elements.keys()
        epI = self._GF.getElementPointIPerTrueElement( GD, segElements )
        gObj = objMaker(self._GF, self._data, self._dataWeights,
                        nClosestPoints=nClosestPoints)

        # get initial transform
        if self._TFitted is None:
            x0 = self._TFitted.getT()
        else:
            x0 = self._T.getT()

        if len(x0) < reqNParams:
            x0 = np.hstack([x0, np.zeros(reqNParams - len(x0))])
        elif len(x0) > reqNParams:
            x0 = x0[:reqNParams]

        # fit
        if fitScale:
            GXOpt, GPOpt = PCFitter.rigidScaleModeNFit(gObj, modes=fitModes[1:],
                                                       x0=x0, mWeight=mWeight
                                                       )
        else:
            GXOpt, GPOpt = PCFitter.rigidModeNFit(gObj, modes=fitModes[1:],
                                                  x0=x0, mWeight=mWeight
                                                  )
        GF.set_field_parameters(GPOpt.copy().reshape((3,-1,1)))
        # error calculation
        self._fitError = obj(GPOpt.copy())
        self._RMSEFitted = np.sqrt(self._fitError.mean())
        # transform and GF
        self._TFitted = transformations.RigidPCModesTransform(GXOpt)
        self._GFFitted = copy.deepcopy(self._GF)
        return self._GFFitted, self._TFitted, self._RMSEFitted, self._fitErrors

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''

        # Put your execute step code here before calling the '_doneExecution' method.
        if self._config['GUI']:
            self._widget = MayaviPCMeshFittingViewerWidget(
                                self._data,
                                self._GFUnfitted,
                                self._config,
                                self._fit,
                                self._reset,
                                self._distModes)
            
            # self._widget._ui.registerButton.clicked.connect(self._register)
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget._ui.resetButton.clicked.connect(self._reset)
            self._widget.setModal(True)
            self._setCurrentWidget(self._widget)

        else:
            self._fit()
            self.GFFitted = copy.deepcopy(self.GF)
            self._doneExecution()

    def _abort(self):
        # self._doneExecution()
        raise RuntimeError, 'mesh fitting aborted'

    def _reset(self):
        self._GFFitted = None
        self._TFitted = None
        self._RMSEFitted = None
        self._fitErrors = None
        self.GF = copy.deepcopy(self.GFUnfitted)

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''

        ######## TODO  BELOW  #############

        if index == 0:
            self._data = dataIn # ju#pointcoordinates
        elif index == 1:
            self._GF = dataIn   # ju#fieldworkmodel
            self._GFUnfitted = copy.deepcopy(self._GF)
        elif index == 2:
            self._pc = dataIn   # ju#principalcomponents
        elif index == 3:
            self._T0 = dataIn
        else:
            self.dataWeights = dataIn # numpyarray1d - dataWeights

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 5:
            return self.GFFitted # ju#fieldworkmodel
        elif index == 6:
            return self._TFitted # ju#geometrictransform
        elif index == 7:
            return self._RMSEFitted # float
        else:
            return self._fitErrors # numpyarray1d

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog(self._distModes)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)
        
        if dlg.exec_():
            self._config = dlg.getConfig()
        
        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self, location):
        '''
        Add code to serialize this step to disk.  The filename should
        use the step identifier (received from getIdentifier()) to keep it
        unique within the workflow.  The suggested name for the file on
        disk is:
            filename = getIdentifier() + '.conf'
        '''
        configuration_file = os.path.join(location, self.getIdentifier() + '.conf')
        conf = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        conf.beginGroup('config')
        for k in self._config.keys():
            conf.setValue(k, self._config[k])
        
        if self._config['Fit Scale']:
            conf.setValue('Fit Scale', 'True')
        else:
            conf.setValue('Fit Scale', 'False')  

        if self._config['GUI']:
            conf.setValue('GUI', 'True')
        else:
            conf.setValue('GUI', 'False')    

        conf.endGroup()

    def deserialize(self, location):
        '''
        Add code to deserialize this step from disk.  As with the serialize 
        method the filename should use the step identifier.  Obviously the 
        filename used here should be the same as the one used by the
        serialize method.
        '''
        configuration_file = os.path.join(location, self.getIdentifier() + '.conf')
        conf = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        conf.beginGroup('config')

        for k, v in self._configDefaults.items():
            self._config[k] = conf.value(k, v)

        if conf.value('Fit Scale')=='True':
            self._config['Fit Scale'] = True
        elif conf.value('Fit Scale')=='False':
            self._config['Fit Scale'] = False

        if conf.value('GUI')=='True':
            self._config['GUI'] = True
        elif conf.value('GUI')=='False':
            self._config['GUI'] = False

        conf.endGroup()

        d = ConfigureDialog(self._distModes)
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()

