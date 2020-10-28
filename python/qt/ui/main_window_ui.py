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
        MainWindow.resize(640, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.fSetup = QtWidgets.QFrame(self.splitter)
        self.fSetup.setObjectName("fSetup")
        self.gridLayout = QtWidgets.QGridLayout(self.fSetup)
        self.gridLayout.setObjectName("gridLayout")
        self.pbEdit = QtWidgets.QPushButton(self.fSetup)
        self.pbEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.pbEdit.setMaximumSize(QtCore.QSize(30, 30))
        self.pbEdit.setText("")
        self.pbEdit.setCheckable(True)
        self.pbEdit.setChecked(True)
        self.pbEdit.setObjectName("pbEdit")
        self.gridLayout.addWidget(self.pbEdit, 0, 8, 1, 1)
        self.pbAddBody = QtWidgets.QPushButton(self.fSetup)
        self.pbAddBody.setMinimumSize(QtCore.QSize(30, 30))
        self.pbAddBody.setMaximumSize(QtCore.QSize(30, 30))
        self.pbAddBody.setText("")
        self.pbAddBody.setObjectName("pbAddBody")
        self.gridLayout.addWidget(self.pbAddBody, 0, 6, 1, 1)
        self.lbDuration = QtWidgets.QLabel(self.fSetup)
        self.lbDuration.setObjectName("lbDuration")
        self.gridLayout.addWidget(self.lbDuration, 0, 2, 1, 1)
        self.lbTimeStep = QtWidgets.QLabel(self.fSetup)
        self.lbTimeStep.setObjectName("lbTimeStep")
        self.gridLayout.addWidget(self.lbTimeStep, 0, 0, 1, 1)
        self.dsbTimeStep = QtWidgets.QDoubleSpinBox(self.fSetup)
        self.dsbTimeStep.setDecimals(2)
        self.dsbTimeStep.setProperty("value", 1.0)
        self.dsbTimeStep.setObjectName("dsbTimeStep")
        self.gridLayout.addWidget(self.dsbTimeStep, 0, 1, 1, 1)
        self.twBodyData = QtWidgets.QTableWidget(self.fSetup)
        self.twBodyData.setStyleSheet("QHeaderView::section {\n"
"    font-size: 10pt;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px;\n"
"    border: 1px solid #828790;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"}\n"
"\n"
"QHeaderView::section::last {\n"
"    border-right: 0px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    font-size: 8pt;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    background-color: #c7e0ff;\n"
"    color: #000000;\n"
"}")
        self.twBodyData.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twBodyData.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twBodyData.setShowGrid(False)
        self.twBodyData.setObjectName("twBodyData")
        self.twBodyData.setColumnCount(6)
        self.twBodyData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyData.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyData.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBodyData.setHorizontalHeaderItem(5, item)
        self.twBodyData.horizontalHeader().setHighlightSections(False)
        self.twBodyData.horizontalHeader().setStretchLastSection(True)
        self.twBodyData.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.twBodyData, 1, 0, 1, 12)
        self.dsbDuration = QtWidgets.QDoubleSpinBox(self.fSetup)
        self.dsbDuration.setDecimals(2)
        self.dsbDuration.setMinimum(1.0)
        self.dsbDuration.setMaximum(5000.0)
        self.dsbDuration.setProperty("value", 500.0)
        self.dsbDuration.setObjectName("dsbDuration")
        self.gridLayout.addWidget(self.dsbDuration, 0, 3, 1, 1)
        self.pbPlayPause = QtWidgets.QPushButton(self.fSetup)
        self.pbPlayPause.setMinimumSize(QtCore.QSize(30, 30))
        self.pbPlayPause.setMaximumSize(QtCore.QSize(30, 30))
        self.pbPlayPause.setText("")
        self.pbPlayPause.setObjectName("pbPlayPause")
        self.gridLayout.addWidget(self.pbPlayPause, 0, 11, 1, 1)
        self.pbStop = QtWidgets.QPushButton(self.fSetup)
        self.pbStop.setMinimumSize(QtCore.QSize(30, 30))
        self.pbStop.setMaximumSize(QtCore.QSize(30, 30))
        self.pbStop.setText("")
        self.pbStop.setObjectName("pbStop")
        self.gridLayout.addWidget(self.pbStop, 0, 10, 1, 1)
        self.line = QtWidgets.QFrame(self.fSetup)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 9, 1, 1)
        self.fControls = QtWidgets.QFrame(self.fSetup)
        self.fControls.setObjectName("fControls")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fControls)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addWidget(self.fControls, 4, 0, 1, 7)
        self.pbRemoveBody = QtWidgets.QPushButton(self.fSetup)
        self.pbRemoveBody.setMinimumSize(QtCore.QSize(30, 30))
        self.pbRemoveBody.setMaximumSize(QtCore.QSize(30, 30))
        self.pbRemoveBody.setText("")
        self.pbRemoveBody.setObjectName("pbRemoveBody")
        self.gridLayout.addWidget(self.pbRemoveBody, 0, 5, 1, 1)
        self.tbTimeSettings = QtWidgets.QToolButton(self.fSetup)
        self.tbTimeSettings.setMinimumSize(QtCore.QSize(30, 30))
        self.tbTimeSettings.setMaximumSize(QtCore.QSize(30, 30))
        self.tbTimeSettings.setText("")
        self.tbTimeSettings.setObjectName("tbTimeSettings")
        self.gridLayout.addWidget(self.tbTimeSettings, 0, 7, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.plotLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setObjectName("plotLayout")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "N-Body Simulations"))
        self.pbEdit.setToolTip(_translate("MainWindow", "Interactive Mode"))
        self.pbAddBody.setToolTip(_translate("MainWindow", "Add Body"))
        self.lbDuration.setText(_translate("MainWindow", "Duration: "))
        self.lbTimeStep.setText(_translate("MainWindow", "Time Step: "))
        self.dsbTimeStep.setSuffix(_translate("MainWindow", " d"))
        item = self.twBodyData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.twBodyData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mass (M*)"))
        item = self.twBodyData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "X (au)"))
        item = self.twBodyData.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Y (au)"))
        item = self.twBodyData.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Vx (au/d)"))
        item = self.twBodyData.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Vy (au/d)"))
        self.dsbDuration.setSuffix(_translate("MainWindow", " d"))
        self.pbPlayPause.setToolTip(_translate("MainWindow", "Play"))
        self.pbStop.setToolTip(_translate("MainWindow", "Stop"))
        self.pbRemoveBody.setToolTip(_translate("MainWindow", "Remove Selected Body"))
        self.tbTimeSettings.setToolTip(_translate("MainWindow", "Time Settings"))
