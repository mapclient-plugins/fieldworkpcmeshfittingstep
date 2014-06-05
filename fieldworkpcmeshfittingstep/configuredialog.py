

from PySide import QtGui
from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox
from fieldworkpcmeshfittingstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''

class ConfigureDialog(QtGui.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, distModes, parent=None):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self, parent)
        
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._distModes = distModes
        self._setupDialog()
        self._makeConnections()

    def _setupDialog(self):
        for m in self._distModes:
            self._ui.comboBoxDistanceMode.addItem(m)

        self._ui.lineEditXTol.setValidator(QtGui.QDoubleValidator())
        self._ui.spinBoxPCsToFit.setSingleStep(1)
        self._ui.spinBoxSurfDisc.setSingleStep(1)
        self._ui.doubleSpinBoxMWeight.setSingleStep(0.1)
        self._ui.spinBoxMaxfev.setMaximum(10000)
        self._ui.spinBoxMaxfev.setSingleStep(100)
        self._ui.spinBoxNCP.setSingleStep(1)


    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtGui.QMessageBox.Yes
        if not self.validate():
            result = QtGui.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if result == QtGui.QMessageBox.Yes:
            QtGui.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)
        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        config['Distance Mode'] = self._ui.comboBoxDistanceMode.currentText()
        config['PCs to Fit'] = self._ui.spinBoxPCsToFit.value()
        config['Surface Discretisation'] = self._ui.spinBoxSurfDisc.value()
        config['Mahalanobis Weight'] = self._ui.doubleSpinBoxMWeight.value()
        config['Max Func Evaluations'] = self._ui.spinBoxMaxfev.value()
        config['xtol'] = self._ui.lineEditXTol.text()
        config['Fit Scale'] = self._ui.checkBoxFitSize.isChecked()
        config['N Closest Points'] = self._ui.spinBoxNCP.value()
        config['GUI'] = self._ui.checkBoxGUI.isChecked()
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        self._ui.comboBoxDistanceMode.setCurrentIndex(self._distModes.index(config['Distance Mode']))
        self._ui.spinBoxPCsToFit.setValue(int(config['PCs to Fit']))
        self._ui.doubleSpinBoxMWeight.setValue(float(config['Mahalanobis Weight']))
        self._ui.spinBoxSurfDisc.setValue(int(config['Surface Discretisation']))
        self._ui.spinBoxMaxfev.setValue(int(config['Max Func Evaluations']))
        self._ui.lineEditXTol.setText(config['xtol'])
        self._ui.checkBoxFitSize.setChecked(bool(config['Fit Scale']))
        self._ui.spinBoxNCP.setValue(int(config['N Closest Points']))
        self._ui.checkBoxGUI.setChecked(bool(config['GUI']))

