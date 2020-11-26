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
        MainWindow.resize(658, 963)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fSetup = QtWidgets.QFrame(self.centralwidget)
        self.fSetup.setObjectName("fSetup")
        self.gridLayout = QtWidgets.QGridLayout(self.fSetup)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.pbShowVelocityArrows = QtWidgets.QPushButton(self.fSetup)
        self.pbShowVelocityArrows.setMinimumSize(QtCore.QSize(30, 30))
        self.pbShowVelocityArrows.setMaximumSize(QtCore.QSize(30, 30))
        self.pbShowVelocityArrows.setText("")
        self.pbShowVelocityArrows.setCheckable(True)
        self.pbShowVelocityArrows.setChecked(True)
        self.pbShowVelocityArrows.setObjectName("pbShowVelocityArrows")
        self.gridLayout.addWidget(self.pbShowVelocityArrows, 0, 6, 1, 1)
        self.cbVelocityArrowMagnification = QtWidgets.QComboBox(self.fSetup)
        self.cbVelocityArrowMagnification.setMinimumSize(QtCore.QSize(42, 28))
        self.cbVelocityArrowMagnification.setMaximumSize(QtCore.QSize(42, 28))
        self.cbVelocityArrowMagnification.setFrame(True)
        self.cbVelocityArrowMagnification.setObjectName("cbVelocityArrowMagnification")
        self.cbVelocityArrowMagnification.addItem("")
        self.cbVelocityArrowMagnification.addItem("")
        self.cbVelocityArrowMagnification.addItem("")
        self.cbVelocityArrowMagnification.addItem("")
        self.cbVelocityArrowMagnification.addItem("")
        self.cbVelocityArrowMagnification.addItem("")
        self.cbVelocityArrowMagnification.addItem("")
        self.gridLayout.addWidget(self.cbVelocityArrowMagnification, 0, 5, 1, 1)
        self.pbShowPositionLabels = QtWidgets.QPushButton(self.fSetup)
        self.pbShowPositionLabels.setMinimumSize(QtCore.QSize(30, 30))
        self.pbShowPositionLabels.setMaximumSize(QtCore.QSize(30, 30))
        self.pbShowPositionLabels.setText("")
        self.pbShowPositionLabels.setCheckable(True)
        self.pbShowPositionLabels.setChecked(True)
        self.pbShowPositionLabels.setObjectName("pbShowPositionLabels")
        self.gridLayout.addWidget(self.pbShowPositionLabels, 0, 7, 1, 1)
        self.line = QtWidgets.QFrame(self.fSetup)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 9, 1, 1)
        self.pbPlayPause = QtWidgets.QPushButton(self.fSetup)
        self.pbPlayPause.setMinimumSize(QtCore.QSize(30, 30))
        self.pbPlayPause.setMaximumSize(QtCore.QSize(30, 30))
        self.pbPlayPause.setText("")
        self.pbPlayPause.setObjectName("pbPlayPause")
        self.gridLayout.addWidget(self.pbPlayPause, 0, 11, 1, 1)
        self.pbRemoveBody = QtWidgets.QPushButton(self.fSetup)
        self.pbRemoveBody.setMinimumSize(QtCore.QSize(30, 30))
        self.pbRemoveBody.setMaximumSize(QtCore.QSize(30, 30))
        self.pbRemoveBody.setText("")
        self.pbRemoveBody.setObjectName("pbRemoveBody")
        self.gridLayout.addWidget(self.pbRemoveBody, 0, 1, 1, 1)
        self.tbAddBody = QtWidgets.QToolButton(self.fSetup)
        self.tbAddBody.setMinimumSize(QtCore.QSize(30, 30))
        self.tbAddBody.setMaximumSize(QtCore.QSize(30, 30))
        self.tbAddBody.setText("")
        self.tbAddBody.setObjectName("tbAddBody")
        self.gridLayout.addWidget(self.tbAddBody, 0, 2, 1, 1)
        self.pbInteractiveMode = QtWidgets.QPushButton(self.fSetup)
        self.pbInteractiveMode.setMinimumSize(QtCore.QSize(30, 30))
        self.pbInteractiveMode.setMaximumSize(QtCore.QSize(30, 30))
        self.pbInteractiveMode.setText("")
        self.pbInteractiveMode.setCheckable(True)
        self.pbInteractiveMode.setChecked(True)
        self.pbInteractiveMode.setObjectName("pbInteractiveMode")
        self.gridLayout.addWidget(self.pbInteractiveMode, 0, 8, 1, 1)
        self.pbStop = QtWidgets.QPushButton(self.fSetup)
        self.pbStop.setMinimumSize(QtCore.QSize(30, 30))
        self.pbStop.setMaximumSize(QtCore.QSize(30, 30))
        self.pbStop.setText("")
        self.pbStop.setObjectName("pbStop")
        self.gridLayout.addWidget(self.pbStop, 0, 10, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.fSetup)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 4, 1, 1)
        self.tbTimeSettings = QtWidgets.QToolButton(self.fSetup)
        self.tbTimeSettings.setMinimumSize(QtCore.QSize(30, 30))
        self.tbTimeSettings.setMaximumSize(QtCore.QSize(30, 30))
        self.tbTimeSettings.setText("")
        self.tbTimeSettings.setObjectName("tbTimeSettings")
        self.gridLayout.addWidget(self.tbTimeSettings, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.fSetup)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.fBodyDataTable = QtWidgets.QFrame(self.splitter)
        self.fBodyDataTable.setStyleSheet("QFrame {\n"
"    border: 1px solid #828790;\n"
"}")
        self.fBodyDataTable.setObjectName("fBodyDataTable")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fBodyDataTable)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.twBodyColours = QtWidgets.QTableWidget(self.fBodyDataTable)
        self.twBodyColours.setMinimumSize(QtCore.QSize(30, 0))
        self.twBodyColours.setMaximumSize(QtCore.QSize(30, 16777215))
        self.twBodyColours.setStyleSheet("QHeaderView::section {\n"
"    font-size: 10pt;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px;\n"
"    border: 1px solid #828790;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"}")
        self.twBodyColours.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.twBodyColours.setObjectName("twBodyColours")
        self.twBodyColours.setColumnCount(1)
        self.twBodyColours.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyColours.setHorizontalHeaderItem(0, item)
        self.twBodyColours.horizontalHeader().setStretchLastSection(True)
        self.twBodyColours.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.twBodyColours)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "N-Body Simulations"))
        self.pbShowVelocityArrows.setToolTip(_translate("MainWindow", "Show Body Velocity Arrows"))
        self.cbVelocityArrowMagnification.setToolTip(_translate("MainWindow", "The factor to magnify the velocity arrows by"))
        self.cbVelocityArrowMagnification.setItemText(0, _translate("MainWindow", "x1"))
        self.cbVelocityArrowMagnification.setItemText(1, _translate("MainWindow", "x2"))
        self.cbVelocityArrowMagnification.setItemText(2, _translate("MainWindow", "x4"))
        self.cbVelocityArrowMagnification.setItemText(3, _translate("MainWindow", "x8"))
        self.cbVelocityArrowMagnification.setItemText(4, _translate("MainWindow", "x16"))
        self.cbVelocityArrowMagnification.setItemText(5, _translate("MainWindow", "x32"))
        self.cbVelocityArrowMagnification.setItemText(6, _translate("MainWindow", "x64"))
        self.pbShowPositionLabels.setToolTip(_translate("MainWindow", "Show Body Coordinate Labels"))
        self.pbPlayPause.setToolTip(_translate("MainWindow", "Play"))
        self.pbRemoveBody.setToolTip(_translate("MainWindow", "Remove Selected Body"))
        self.tbAddBody.setToolTip(_translate("MainWindow", "Add Body Options"))
        self.pbInteractiveMode.setToolTip(_translate("MainWindow", "Interactive Mode"))
        self.pbStop.setToolTip(_translate("MainWindow", "Stop"))
        self.tbTimeSettings.setToolTip(_translate("MainWindow", "Time Settings"))
