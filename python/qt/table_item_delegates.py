# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml_reader import get_user_interface_property

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QColorDialog, QDoubleSpinBox, QStyledItemDelegate


class ColourItemDelegate(QStyledItemDelegate):
    """A class which creates a custom item delegate for allowing the selection of a QColor from a dialog."""

    def __init__(self, parent):
        """Initializes the item delegate with a None type colour dialog."""
        super(ColourItemDelegate, self).__init__(parent)
        self._colour_dialog = None

    def createEditor(self, parent, style, index) -> None:
        """Overrides the parent method to create a custom QColorDialog."""
        self._colour_dialog = QColorDialog(parent)
        return self._colour_dialog

    def setEditorData(self, editor, index):
        """Sets the QColor displayed in the QColorDialog when it opens."""
        colour = index.data(Qt.BackgroundRole)
        if colour is not None:
            editor.setCurrentColor(colour)

    def setModelData(self, editor, model, index):
        """Sets the QColor displayed in the QItemDelegate when the QColorDialog is closed."""
        if self._colour_dialog.result():
            colour = editor.currentColor()
            model.setData(index, colour, Qt.BackgroundRole)


class DoubleItemDelegate(QStyledItemDelegate):
    """A class which creates a custom item delegate for managing double data stored in a QTableWidget."""

    Mass = "mass"
    Position = "position"
    Velocity = "velocity"

    def __init__(self, parent, item_type: str):
        """Initializes the item delegate using the properties stored in the user interface properties file."""
        super(DoubleItemDelegate, self).__init__(parent)

        self.min = float(get_user_interface_property(item_type + "-min"))
        self.max = float(get_user_interface_property(item_type + "-max"))
        self.step = float(get_user_interface_property(item_type + "-step"))
        self.decimals = int(get_user_interface_property(item_type + "-dp"))

    def createEditor(self, parent, style, index) -> None:
        """Overrides the parent method to create a custom QDoubleSpinBox."""
        box = QDoubleSpinBox(parent)
        box.setDecimals(self.decimals)

        box.setSingleStep(self.step)
        box.setMinimum(self.min)
        box.setMaximum(self.max)

        return box
