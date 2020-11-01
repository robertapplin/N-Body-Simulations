# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml_reader import get_user_interface_property

from PyQt5.QtWidgets import QDoubleSpinBox, QStyledItemDelegate


class TableItemDelegate(QStyledItemDelegate):
    """A class which creates a custom item delegate for managing the data stored in a QTableWidget."""

    Mass = "mass"
    Position = "position"
    Velocity = "velocity"

    def __init__(self, parent, item_type: str):
        """Initializes the item delegate using the properties stored in the user interface properties file."""
        super(TableItemDelegate, self).__init__(parent)

        self._min = float(get_user_interface_property(item_type + "-min"))
        self._max = float(get_user_interface_property(item_type + "-max"))
        self._step = float(get_user_interface_property(item_type + "-step"))
        self._decimals = int(get_user_interface_property(item_type + "-dp"))

    def createEditor(self, parent, style, index) -> None:
        """Overrides the parent method to create a custom QDoubleSpinBox."""
        box = QDoubleSpinBox(parent)
        box.setDecimals(self._decimals)

        box.setSingleStep(self._step)
        box.setMinimum(self._min)
        box.setMaximum(self._max)

        return box
