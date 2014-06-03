
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
from workutils import fieldwork_seg_tools as fst
from mappluginutils.datatypes import transformations
import numpy as np

class FieldworkPCMeshFittingStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    # maps config keys to fitting function argument names
    _fitConfigDict = {}
    _fitConfigDict['Surface Discretisation'] = 'GD'
    _fitConfigDict['Mahalanobis Weight'] = 'mWeight'
    _fitConfigDict['Max Func Evaluations'] = 'maxfev'
    _fitConfigDict['xtol'] = 'xtol'
    _fitConfigDict['Distance Mode'] = 'gObjType'
    _fitConfigDict['N Closest Points'] = 'nClosestPoints'
    _fitConfigDict['KDtree Args'] = 'treeArgs'

    _configDefaults = {}
    _configDefaults['identifier'] = ''
    _configDefaults['Surface Discretisation'] = '[8,8]'
    _configDefaults['Mahalanobis Weight'] = '0.1'
    _configDefaults['Max Func Evaluations'] = '1000'
    _configDefaults['xtol'] = '1e-6'
    _configDefaults['Distance Mode'] = 'EPDP'
    _configDefaults['N Closest Points'] = '1'
    _configDefaults['KDtree Args'] = '{}'
    _configDefaults['GUI'] = 'True'

    def __init__(self, location):
        super(FieldworkMeshFittingStep, self).__init__('Fieldwork PC Mesh Fitting', location)
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
                      'ju#PrincipalComponents'))

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

    def _makeFitter(self):
        fitkwargs = {}
        if self._config['Distance Mode']=='DPEP':
            fitkwargs['objMaker'] = fst.GFF.makeObjDPEP
        elif self._config['Distance Mode']=='EPDP':
            fitkwargs['objMaker'] = fst.GFF.makeObjEPDP
        fitkwargs['SSM'] = self._pc
        fitkwargs['SSMModes'] = [int(i) for i in self._config['Fit PCs'].split(',')]
        fitkwargs['GF'] = self._GF
        fitkwargs['GD'] = [int(i) for i in self._config['Surface Discretisation'].split(',')]
        fitkwargs['mahalanobisWeight'] = float(self._config['Mahalanobis Weight'])
        fitkwargs['epIndex'] = None
        fitkwargs['GFCoordEval'] = None
        fitkwargs['retFullError'] = True
        
        self._fitter = fst._makeMeshFitPCFit(**kwargs)

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''

        # Put your execute step code here before calling the '_doneExecution' method.
        if self._config['GUI']=='True':
            self._widget = MayaviPCMeshFittingViewerWidget(
                                self.data,
                                self.GFUnfitted,
                                self._config,
                                self._fit,
                                self._reset)
            
            # self._widget._ui.registerButton.clicked.connect(self._register)
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget._ui.resetButton.clicked.connect(self._reset)
            self._widget.setModal(True)
            self._setCurrentWidget(self._widget)

        elif self._config['GUI']=='False':
            self._fit()
            self.GFFitted = copy.deepcopy(self.GF)
            self._doneExecution()

    def _fit(self, callback=None):

        # generate fitting function
        self._makeFitter()

        # call fitting functions
        x0 = self._T0.getT()
        xOpt, self._RMSEFitted, sdFitted, fitErrors = self._fitter(
                                                        self._data,
                                                        x0,
                                                        self._dataWeights
                                                        )

        self._GFFitted = copy.deepcopy(self._GF)
        self._TFitted = transformations.RigidPCModesTransform(xOpt)
        self._fitErrors = np.sqrt(fitErrros)

        return self._GFFitted, self._TFitted, self._RMSEFitted, self._fitErrors

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
            self.data = dataIn # ju#pointcoordinates
        elif index == 1:
            self.GF = dataIn   # ju#fieldworkmodel
            self.GFUnfitted = copy.deepcopy(self.GF)
        else:
            self.dataWeights = dataIn # numpyarray1d - dataWeights

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 3:
            return self.GFFitted # ju#fieldworkmodel
        elif index == 4:
            return self.GFParamsFitted # ju#fieldworkmodelparameters
        elif index == 5:
            return self.RMSEFitted # float
        else:
            return self.fitErrors # numpyarray1d

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
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
        # conf.setValue('identifier', self._config['identifier'])
        # conf.setValue('GD', self._config['GD'])
        # conf.setValue('sobelovD', self._config['sobelovD'])
        # conf.setValue('sobelovW', self._config['sobelovW'])
        # conf.setValue('normalD', self._config['normalD'])
        # conf.setValue('normalW', self._config['normalW'])
        # conf.setValue('itMaxPerIt', self._config['itMaxPerIt'])
        # conf.setValue('xtol', self._config['xtol'])
        # conf.setValue('itMax', self._config['itMax'])
        # conf.setValue('mode', self._config['mode'])
        # conf.setValue('nClosestPoints', self._config['nClosestPoints'])
        # conf.setValue('treeArgs', self._config['treeArgs'])
        # conf.setValue('fitVerbose', self._config['fitVerbose'])
        # conf.setValue('fixedNodes', self._config['fixedNodes'])
        # conf.setValue('GUI', self._config['GUI'])
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
        # self._config['identifier'] = conf.value('identifier', '')
        # self._config['GD'] = conf.value('GD', '5.0')
        # self._config['sobelovD'] = conf.value('sobelovD', '[8,8]')
        # self._config['sobelovW'] = conf.value('sobelovW', '[1e-6, 1e-6, 1e-6, 1e-6, 2e-6]')
        # self._config['normalD'] = conf.value('normalD', '8')
        # self._config['normalW'] = conf.value('normalW', '50.0')
        # self._config['itMaxPerIt'] = conf.value('itMaxPerIt', '3')
        # self._config['xtol'] = conf.value('xtol', '1e-6')
        # self._config['itMax'] = conf.value('itMax', '5')
        # self._config['mode'] = conf.value('mode', 'DPEP')
        # self._config['nClosestPoints'] = conf.value('nClosestPoints', '1')
        # self._config['treeArgs'] = conf.value('treeArgs', '{}')
        # self._config['fitVerbose'] = conf.value('fitVerbose', 'True')
        # self._config['fixedNodes'] = conf.value('fixedNodes', 'None')
        # self._config['GUI'] = conf.value('GUI', 'True')
        conf.endGroup()

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()

