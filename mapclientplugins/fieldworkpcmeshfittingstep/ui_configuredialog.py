# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 491)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label9 = QLabel(self.configGroupBox)
        self.label9.setObjectName(u"label9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label9)

        self.comboBoxDistanceMode = QComboBox(self.configGroupBox)
        self.comboBoxDistanceMode.setObjectName(u"comboBoxDistanceMode")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxDistanceMode)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label1)

        self.label2 = QLabel(self.configGroupBox)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label2)

        self.label3 = QLabel(self.configGroupBox)
        self.label3.setObjectName(u"label3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label3)

        self.label4 = QLabel(self.configGroupBox)
        self.label4.setObjectName(u"label4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label4)

        self.label5 = QLabel(self.configGroupBox)
        self.label5.setObjectName(u"label5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label5)

        self.label8 = QLabel(self.configGroupBox)
        self.label8.setObjectName(u"label8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label8)

        self.label10 = QLabel(self.configGroupBox)
        self.label10.setObjectName(u"label10")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label10)

        self.label14 = QLabel(self.configGroupBox)
        self.label14.setObjectName(u"label14")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label14)

        self.checkBoxGUI = QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setObjectName(u"checkBoxGUI")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.checkBoxGUI)

        self.checkBoxFitSize = QCheckBox(self.configGroupBox)
        self.checkBoxFitSize.setObjectName(u"checkBoxFitSize")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.checkBoxFitSize)

        self.spinBoxPCsToFit = QSpinBox(self.configGroupBox)
        self.spinBoxPCsToFit.setObjectName(u"spinBoxPCsToFit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBoxPCsToFit)

        self.spinBoxSurfDisc = QSpinBox(self.configGroupBox)
        self.spinBoxSurfDisc.setObjectName(u"spinBoxSurfDisc")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.spinBoxSurfDisc)

        self.doubleSpinBoxMWeight = QDoubleSpinBox(self.configGroupBox)
        self.doubleSpinBoxMWeight.setObjectName(u"doubleSpinBoxMWeight")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBoxMWeight)

        self.spinBoxMaxfev = QSpinBox(self.configGroupBox)
        self.spinBoxMaxfev.setObjectName(u"spinBoxMaxfev")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spinBoxMaxfev)

        self.spinBoxNCP = QSpinBox(self.configGroupBox)
        self.spinBoxNCP.setObjectName(u"spinBoxNCP")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.spinBoxNCP)

        self.lineEditXTol = QLineEdit(self.configGroupBox)
        self.lineEditXTol.setObjectName(u"lineEditXTol")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEditXTol)

        self.lineEditLandmarks = QLineEdit(self.configGroupBox)
        self.lineEditLandmarks.setObjectName(u"lineEditLandmarks")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEditLandmarks)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_2)

        self.lineEditLandmarkWeights = QLineEdit(self.configGroupBox)
        self.lineEditLandmarkWeights.setObjectName(u"lineEditLandmarkWeights")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.lineEditLandmarkWeights)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label9.setText(QCoreApplication.translate("Dialog", u"Distance Mode:", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"PCs to Fit:", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"Surface Discretisation:", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"Mahalanobis Weight:", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"Max Func Eval:", None))
        self.label5.setText(QCoreApplication.translate("Dialog", u"xtol:", None))
        self.label8.setText(QCoreApplication.translate("Dialog", u"Fit Size:", None))
        self.label10.setText(QCoreApplication.translate("Dialog", u"N Closest Points:  ", None))
        self.label14.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.checkBoxGUI.setText("")
        self.checkBoxFitSize.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Landmarks:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Landmark Weights:", None))
    # retranslateUi

