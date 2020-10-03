# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtWidgets import QDialog

from qt.ui.add_body_dialog_ui import Ui_AddBodyDialog


class AddBodyDialog(Ui_AddBodyDialog, QDialog):
    """A class for displaying a QDialog to retrieve data for a new body."""

    def __init__(self):
        """Initialize the AddBodyDialog with empty body parameters."""
        super(AddBodyDialog, self).__init__()
        self.setupUi(self)

        self.pbCancel.clicked.connect(self.handle_cancel_clicked)
        self.pbAdd.clicked.connect(self.handle_add_clicked)

        self._name = None
        self._mass = None
        self._x = None
        self._y = None

    def handle_cancel_clicked(self) -> None:
        """Close the QDialog without saving the data."""
        self.close()

    def handle_add_clicked(self) -> None:
        """Save the new body data when Add is clicked and close."""
        if self.leBodyName.text():
            self._name = self.leBodyName.text()
            self._mass = self.dsbMass.value()
            self._x = self.dsbXPosition.value()
            self._y = self.dsbYPosition.value()
            self.close()

    def new_body_data(self) -> tuple:
        """Return the data for the new body."""
        return self._name, self._mass, self._x, self._y
