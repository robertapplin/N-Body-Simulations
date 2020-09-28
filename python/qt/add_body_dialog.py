# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5 import QtWidgets

from qt.ui.add_body_dialog_ui import Ui_AddBodyDialog


class AddBodyDialog(Ui_AddBodyDialog, QtWidgets.QDialog):

    def __init__(self):
        super(AddBodyDialog, self).__init__()
        self.setupUi(self)

        self.pbCancel.clicked.connect(self.handle_cancel_clicked)
        self.pbAdd.clicked.connect(self.handle_add_clicked)

        self._new_body_name = None

    def handle_cancel_clicked(self) -> None:
        self.close()

    def handle_add_clicked(self) -> None:
        if self.leBodyName.text():
            self._new_body_name = self.leBodyName.text()
            self.close()

    def new_body_name(self) -> str:
        return self._new_body_name
