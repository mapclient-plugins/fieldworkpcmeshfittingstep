# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mayavifittingviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mayaviscenewidget import MayaviSceneWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1087, 771)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetMain = QWidget(Dialog)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widgetMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.widgetMain)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(350, 0))
        self.widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 150))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.toolBox = QToolBox(self.widget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_fitting = QWidget()
        self.page_fitting.setObjectName(u"page_fitting")
        self.page_fitting.setGeometry(QRect(0, 0, 307, 529))
        self.verticalLayout = QVBoxLayout(self.page_fitting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.page_fitting)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBoxDistanceMode = QComboBox(self.groupBox)
        self.comboBoxDistanceMode.setObjectName(u"comboBoxDistanceMode")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBoxDistanceMode)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinBoxPCsToFit = QSpinBox(self.groupBox)
        self.spinBoxPCsToFit.setObjectName(u"spinBoxPCsToFit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBoxPCsToFit)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.spinBoxSurfDisc = QSpinBox(self.groupBox)
        self.spinBoxSurfDisc.setObjectName(u"spinBoxSurfDisc")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinBoxSurfDisc)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.doubleSpinBoxMWeight = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxMWeight.setObjectName(u"doubleSpinBoxMWeight")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBoxMWeight)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.spinBoxMaxfev = QSpinBox(self.groupBox)
        self.spinBoxMaxfev.setObjectName(u"spinBoxMaxfev")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.spinBoxMaxfev)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.checkBoxFitSize = QCheckBox(self.groupBox)
        self.checkBoxFitSize.setObjectName(u"checkBoxFitSize")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.checkBoxFitSize)

        self.lineEditXTol = QLineEdit(self.groupBox)
        self.lineEditXTol.setObjectName(u"lineEditXTol")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lineEditXTol)

        self.lineEditLandmarks = QLineEdit(self.groupBox)
        self.lineEditLandmarks.setObjectName(u"lineEditLandmarks")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.lineEditLandmarks)

        self.lineEditLandmarkWeights = QLineEdit(self.groupBox)
        self.lineEditLandmarkWeights.setObjectName(u"lineEditLandmarkWeights")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.lineEditLandmarkWeights)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_9)


        self.verticalLayout.addWidget(self.groupBox)

        self.fitButtonsGroup = QGridLayout()
        self.fitButtonsGroup.setObjectName(u"fitButtonsGroup")
        self.acceptButton = QPushButton(self.page_fitting)
        self.acceptButton.setObjectName(u"acceptButton")

        self.fitButtonsGroup.addWidget(self.acceptButton, 1, 1, 1, 1)

        self.resetButton = QPushButton(self.page_fitting)
        self.resetButton.setObjectName(u"resetButton")

        self.fitButtonsGroup.addWidget(self.resetButton, 0, 1, 1, 1)

        self.abortButton = QPushButton(self.page_fitting)
        self.abortButton.setObjectName(u"abortButton")

        self.fitButtonsGroup.addWidget(self.abortButton, 1, 0, 1, 1)

        self.fitButton = QPushButton(self.page_fitting)
        self.fitButton.setObjectName(u"fitButton")

        self.fitButtonsGroup.addWidget(self.fitButton, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.fitButtonsGroup)

        self.errorGroup = QGroupBox(self.page_fitting)
        self.errorGroup.setObjectName(u"errorGroup")
        self.formLayout_2 = QFormLayout(self.errorGroup)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.RMSELabel = QLabel(self.errorGroup)
        self.RMSELabel.setObjectName(u"RMSELabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.RMSELabel)

        self.RMSELineEdit = QLineEdit(self.errorGroup)
        self.RMSELineEdit.setObjectName(u"RMSELineEdit")
        self.RMSELineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.RMSELineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.RMSELineEdit)

        self.meanErrorLabel = QLabel(self.errorGroup)
        self.meanErrorLabel.setObjectName(u"meanErrorLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.meanErrorLabel)

        self.meanErrorLineEdit = QLineEdit(self.errorGroup)
        self.meanErrorLineEdit.setObjectName(u"meanErrorLineEdit")
        self.meanErrorLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.meanErrorLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.meanErrorLineEdit)

        self.SDLabel = QLabel(self.errorGroup)
        self.SDLabel.setObjectName(u"SDLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.SDLabel)

        self.SDLineEdit = QLineEdit(self.errorGroup)
        self.SDLineEdit.setObjectName(u"SDLineEdit")
        self.SDLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SDLineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.SDLineEdit)


        self.verticalLayout.addWidget(self.errorGroup)

        self.toolBox.addItem(self.page_fitting, u"Fitting")
        self.Screenshot = QWidget()
        self.Screenshot.setObjectName(u"Screenshot")
        self.Screenshot.setGeometry(QRect(0, 0, 191, 143))
        self.formLayout = QFormLayout(self.Screenshot)
        self.formLayout.setObjectName(u"formLayout")
        self.pixelsXLabel = QLabel(self.Screenshot)
        self.pixelsXLabel.setObjectName(u"pixelsXLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pixelsXLabel)

        self.screenshotPixelXLineEdit = QLineEdit(self.Screenshot)
        self.screenshotPixelXLineEdit.setObjectName(u"screenshotPixelXLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.screenshotPixelXLineEdit)

        self.pixelsYLabel = QLabel(self.Screenshot)
        self.pixelsYLabel.setObjectName(u"pixelsYLabel")
        sizePolicy2.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pixelsYLabel)

        self.screenshotPixelYLineEdit = QLineEdit(self.Screenshot)
        self.screenshotPixelYLineEdit.setObjectName(u"screenshotPixelYLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.screenshotPixelYLineEdit)

        self.screenshotFilenameLabel = QLabel(self.Screenshot)
        self.screenshotFilenameLabel.setObjectName(u"screenshotFilenameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.screenshotFilenameLabel)

        self.screenshotFilenameLineEdit = QLineEdit(self.Screenshot)
        self.screenshotFilenameLineEdit.setObjectName(u"screenshotFilenameLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.screenshotFilenameLineEdit)

        self.screenshotSaveButton = QPushButton(self.Screenshot)
        self.screenshotSaveButton.setObjectName(u"screenshotSaveButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.screenshotSaveButton)

        self.toolBox.addItem(self.Screenshot, u"Screenshots")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.MayaviScene = MayaviSceneWidget(self.widgetMain)
        self.MayaviScene.setObjectName(u"MayaviScene")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widgetMain)


        self.retranslateUi(Dialog)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Mesh Fitting", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Visible", None));
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Fitting Parameters", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Distance Model:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"PCs to Fit:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Surface Discretisation:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Mahalanobis Weight:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"maxfev:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"xtol:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Fit Size:", None))
        self.checkBoxFitSize.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Landmarks:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Landmark Weights:", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.abortButton.setText(QCoreApplication.translate("Dialog", u"Abort", None))
        self.fitButton.setText(QCoreApplication.translate("Dialog", u"Fit", None))
        self.errorGroup.setTitle(QCoreApplication.translate("Dialog", u"Fitting Errors", None))
        self.RMSELabel.setText(QCoreApplication.translate("Dialog", u"RMS:", None))
        self.meanErrorLabel.setText(QCoreApplication.translate("Dialog", u"Mean:", None))
        self.SDLabel.setText(QCoreApplication.translate("Dialog", u"S.D.:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_fitting), QCoreApplication.translate("Dialog", u"Fitting", None))
        self.pixelsXLabel.setText(QCoreApplication.translate("Dialog", u"Pixels X:", None))
        self.screenshotPixelXLineEdit.setText(QCoreApplication.translate("Dialog", u"800", None))
        self.pixelsYLabel.setText(QCoreApplication.translate("Dialog", u"Pixels Y:", None))
        self.screenshotPixelYLineEdit.setText(QCoreApplication.translate("Dialog", u"600", None))
        self.screenshotFilenameLabel.setText(QCoreApplication.translate("Dialog", u"Filename:", None))
        self.screenshotFilenameLineEdit.setText(QCoreApplication.translate("Dialog", u"screenshot.png", None))
        self.screenshotSaveButton.setText(QCoreApplication.translate("Dialog", u"Save Screenshot", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Screenshot), QCoreApplication.translate("Dialog", u"Screenshots", None))
    # retranslateUi

