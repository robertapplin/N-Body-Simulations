# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fSetup = QtWidgets.QFrame(self.centralwidget)
        self.fSetup.setObjectName("fSetup")
        self.gridLayout = QtWidgets.QGridLayout(self.fSetup)
        self.gridLayout.setObjectName("gridLayout")
        self.pbRemoveBody = QtWidgets.QPushButton(self.fSetup)
        self.pbRemoveBody.setMinimumSize(QtCore.QSize(23, 23))
        self.pbRemoveBody.setMaximumSize(QtCore.QSize(23, 23))
        self.pbRemoveBody.setObjectName("pbRemoveBody")
        self.gridLayout.addWidget(self.pbRemoveBody, 0, 3, 1, 1)
        self.cbBodyNames = QtWidgets.QComboBox(self.fSetup)
        self.cbBodyNames.setMinimumSize(QtCore.QSize(0, 21))
        self.cbBodyNames.setMaximumSize(QtCore.QSize(16777215, 21))
        self.cbBodyNames.setObjectName("cbBodyNames")
        self.cbBodyNames.addItem("")
        self.gridLayout.addWidget(self.cbBodyNames, 0, 0, 1, 3)
        self.pbAddBody = QtWidgets.QPushButton(self.fSetup)
        self.pbAddBody.setMinimumSize(QtCore.QSize(23, 23))
        self.pbAddBody.setMaximumSize(QtCore.QSize(23, 23))
        self.pbAddBody.setObjectName("pbAddBody")
        self.gridLayout.addWidget(self.pbAddBody, 0, 4, 1, 1)
        self.lbMass = QtWidgets.QLabel(self.fSetup)
        self.lbMass.setMinimumSize(QtCore.QSize(30, 0))
        self.lbMass.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lbMass.setObjectName("lbMass")
        self.gridLayout.addWidget(self.lbMass, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.fSetup)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbXPosition = QtWidgets.QLabel(self.frame)
        self.lbXPosition.setMinimumSize(QtCore.QSize(30, 0))
        self.lbXPosition.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lbXPosition.setObjectName("lbXPosition")
        self.horizontalLayout_2.addWidget(self.lbXPosition)
        self.dsbXPosition = QtWidgets.QDoubleSpinBox(self.frame)
        self.dsbXPosition.setMinimumSize(QtCore.QSize(0, 20))
        self.dsbXPosition.setDecimals(6)
        self.dsbXPosition.setMinimum(-100.0)
        self.dsbXPosition.setMaximum(100.0)
        self.dsbXPosition.setObjectName("dsbXPosition")
        self.horizontalLayout_2.addWidget(self.dsbXPosition)
        self.lbYPosition = QtWidgets.QLabel(self.frame)
        self.lbYPosition.setMinimumSize(QtCore.QSize(30, 0))
        self.lbYPosition.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lbYPosition.setObjectName("lbYPosition")
        self.horizontalLayout_2.addWidget(self.lbYPosition)
        self.dsbYPosition = QtWidgets.QDoubleSpinBox(self.frame)
        self.dsbYPosition.setMinimumSize(QtCore.QSize(0, 20))
        self.dsbYPosition.setDecimals(6)
        self.dsbYPosition.setMinimum(-100.0)
        self.dsbYPosition.setMaximum(100.0)
        self.dsbYPosition.setObjectName("dsbYPosition")
        self.horizontalLayout_2.addWidget(self.dsbYPosition)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 5)
        self.frame_2 = QtWidgets.QFrame(self.fSetup)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbXVelocity = QtWidgets.QLabel(self.frame_2)
        self.lbXVelocity.setMinimumSize(QtCore.QSize(30, 0))
        self.lbXVelocity.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lbXVelocity.setObjectName("lbXVelocity")
        self.horizontalLayout_3.addWidget(self.lbXVelocity)
        self.dsbXVelocity = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbXVelocity.setMinimumSize(QtCore.QSize(0, 20))
        self.dsbXVelocity.setDecimals(6)
        self.dsbXVelocity.setMinimum(-100.0)
        self.dsbXVelocity.setMaximum(100.0)
        self.dsbXVelocity.setObjectName("dsbXVelocity")
        self.horizontalLayout_3.addWidget(self.dsbXVelocity)
        self.lbYVelocity = QtWidgets.QLabel(self.frame_2)
        self.lbYVelocity.setMinimumSize(QtCore.QSize(30, 0))
        self.lbYVelocity.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lbYVelocity.setObjectName("lbYVelocity")
        self.horizontalLayout_3.addWidget(self.lbYVelocity)
        self.dsbYVelocity = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.dsbYVelocity.setMinimumSize(QtCore.QSize(0, 20))
        self.dsbYVelocity.setDecimals(6)
        self.dsbYVelocity.setMinimum(-100.0)
        self.dsbYVelocity.setMaximum(100.0)
        self.dsbYVelocity.setObjectName("dsbYVelocity")
        self.horizontalLayout_3.addWidget(self.dsbYVelocity)
        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 5)
        self.dsbMass = QtWidgets.QDoubleSpinBox(self.fSetup)
        self.dsbMass.setMinimumSize(QtCore.QSize(0, 20))
        self.dsbMass.setDecimals(6)
        self.dsbMass.setMinimum(0.01)
        self.dsbMass.setSingleStep(0.1)
        self.dsbMass.setObjectName("dsbMass")
        self.gridLayout.addWidget(self.dsbMass, 2, 1, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.lbTimeStep = QtWidgets.QLabel(self.fSetup)
        self.lbTimeStep.setObjectName("lbTimeStep")
        self.gridLayout.addWidget(self.lbTimeStep, 6, 0, 1, 1)
        self.dsbTimeStep = QtWidgets.QDoubleSpinBox(self.fSetup)
        self.dsbTimeStep.setDecimals(2)
        self.dsbTimeStep.setProperty("value", 1.0)
        self.dsbTimeStep.setObjectName("dsbTimeStep")
        self.gridLayout.addWidget(self.dsbTimeStep, 6, 1, 1, 4)
        self.lbDuration = QtWidgets.QLabel(self.fSetup)
        self.lbDuration.setObjectName("lbDuration")
        self.gridLayout.addWidget(self.lbDuration, 7, 0, 1, 1)
        self.dsbDuration = QtWidgets.QDoubleSpinBox(self.fSetup)
        self.dsbDuration.setDecimals(2)
        self.dsbDuration.setMinimum(1.0)
        self.dsbDuration.setMaximum(5000.0)
        self.dsbDuration.setProperty("value", 500.0)
        self.dsbDuration.setObjectName("dsbDuration")
        self.gridLayout.addWidget(self.dsbDuration, 7, 1, 1, 4)
        self.pbPlayPause = QtWidgets.QPushButton(self.fSetup)
        self.pbPlayPause.setObjectName("pbPlayPause")
        self.gridLayout.addWidget(self.pbPlayPause, 8, 2, 1, 3)
        self.pbStop = QtWidgets.QPushButton(self.fSetup)
        self.pbStop.setObjectName("pbStop")
        self.gridLayout.addWidget(self.pbStop, 8, 0, 1, 2)
        self.horizontalLayout.addWidget(self.fSetup)
        self.plotLayout = QtWidgets.QGridLayout()
        self.plotLayout.setObjectName("plotLayout")
        self.horizontalLayout.addLayout(self.plotLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "N-Body Simulations"))
        self.pbRemoveBody.setText(_translate("MainWindow", "Bin"))
        self.cbBodyNames.setItemText(0, _translate("MainWindow", "Sun"))
        self.pbAddBody.setText(_translate("MainWindow", "+"))
        self.lbMass.setText(_translate("MainWindow", "Mass:"))
        self.lbXPosition.setText(_translate("MainWindow", "X:"))
        self.dsbXPosition.setSuffix(_translate("MainWindow", " au"))
        self.lbYPosition.setText(_translate("MainWindow", "Y:"))
        self.dsbYPosition.setSuffix(_translate("MainWindow", " au"))
        self.lbXVelocity.setText(_translate("MainWindow", "Vx:"))
        self.dsbXVelocity.setSuffix(_translate("MainWindow", " au/d"))
        self.lbYVelocity.setText(_translate("MainWindow", "Vy:"))
        self.dsbYVelocity.setSuffix(_translate("MainWindow", " au/d"))
        self.dsbMass.setSuffix(_translate("MainWindow", " M*"))
        self.lbTimeStep.setText(_translate("MainWindow", "Time Step: "))
        self.dsbTimeStep.setSuffix(_translate("MainWindow", " d"))
        self.lbDuration.setText(_translate("MainWindow", "Duration: "))
        self.dsbDuration.setSuffix(_translate("MainWindow", " d"))
        self.pbPlayPause.setToolTip(_translate("MainWindow", "Play/Pause"))
        self.pbPlayPause.setText(_translate("MainWindow", "Play"))
        self.pbStop.setText(_translate("MainWindow", "Stop"))
