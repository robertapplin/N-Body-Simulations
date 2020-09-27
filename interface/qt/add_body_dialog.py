# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5 import QtWidgets


class AddBodyDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(AddBodyDialog, self).__init__(parent)

        self.setWindowTitle("Add Body Dialog")

        self.lbBodyName = QtWidgets.QLabel("Body name: ")
        self.leBodyName = QtWidgets.QLineEdit()
        self.pbCancel = QtWidgets.QPushButton("Cancel")
        self.pbAdd = QtWidgets.QPushButton("Add")

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.lbBodyName, 1, 0)
        layout.addWidget(self.leBodyName, 1, 1)
        layout.addWidget(self.pbCancel, 2, 0)
        layout.addWidget(self.pbAdd, 2, 1)

        self.setLayout(layout)

        self.pbCancel.clicked.connect(self.handle_cancel_clicked)
        self.pbAdd.clicked.connect(self.handle_add_clicked)

        self._new_body_name = None

    def handle_cancel_clicked(self):
        self.close()

    def handle_add_clicked(self) -> str:
        if self.leBodyName.text():
            self._new_body_name = self.leBodyName.text()
            self.close()

    def new_body_name(self) -> str:
        return self._new_body_name
