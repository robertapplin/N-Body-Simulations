# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_body_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddBodyDialog(object):
    def setupUi(self, AddBodyDialog):
        AddBodyDialog.setObjectName("AddBodyDialog")
        AddBodyDialog.resize(329, 96)
        self.gridLayout = QtWidgets.QGridLayout(AddBodyDialog)
        self.gridLayout.setContentsMargins(20, 20, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.fAddCancel = QtWidgets.QFrame(AddBodyDialog)
        self.fAddCancel.setMinimumSize(QtCore.QSize(30, 0))
        self.fAddCancel.setObjectName("fAddCancel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fAddCancel)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAdd = QtWidgets.QPushButton(self.fAddCancel)
        self.pbAdd.setObjectName("pbAdd")
        self.horizontalLayout.addWidget(self.pbAdd)
        self.pbCancel = QtWidgets.QPushButton(self.fAddCancel)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout.addWidget(self.pbCancel)
        self.gridLayout.addWidget(self.fAddCancel, 3, 0, 1, 2)
        self.lbBodyName = QtWidgets.QLabel(AddBodyDialog)
        self.lbBodyName.setObjectName("lbBodyName")
        self.gridLayout.addWidget(self.lbBodyName, 0, 0, 1, 1)
        self.leBodyName = QtWidgets.QLineEdit(AddBodyDialog)
        self.leBodyName.setObjectName("leBodyName")
        self.gridLayout.addWidget(self.leBodyName, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)

        self.retranslateUi(AddBodyDialog)
        QtCore.QMetaObject.connectSlotsByName(AddBodyDialog)

    def retranslateUi(self, AddBodyDialog):
        _translate = QtCore.QCoreApplication.translate
        AddBodyDialog.setWindowTitle(_translate("AddBodyDialog", "Add Body Dialog"))
        self.pbAdd.setText(_translate("AddBodyDialog", "Add"))
        self.pbCancel.setText(_translate("AddBodyDialog", "Cancel"))
        self.lbBodyName.setText(_translate("AddBodyDialog", "Body name:"))
