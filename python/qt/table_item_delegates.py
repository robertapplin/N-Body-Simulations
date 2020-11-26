# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml_reader import get_user_interface_property

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (QColorDialog, QDoubleSpinBox, QStyle, QStyledItemDelegate, QStyleOptionViewItem,
                             QTableWidget, QTableWidgetItem, QWidget)


class ColourItemDelegate(QStyledItemDelegate):
    """A class which creates a custom item delegate for allowing the selection of a QColor from a dialog."""

    def __init__(self, parent: QTableWidget):
        """Initializes the item delegate with a None type colour dialog."""
        super(ColourItemDelegate, self).__init__(parent)
        self._colour_dialog = None

    def createEditor(self, parent: QWidget, style: QStyleOptionViewItem, index: QModelIndex) -> None:
        """Overrides the parent method to create a custom QColorDialog."""
        self._colour_dialog = QColorDialog(parent)
        return self._colour_dialog

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        """Sets the QColor displayed in the QColorDialog when it opens."""
        colour = index.data(Qt.BackgroundRole)
        if colour is not None:
            editor.setCurrentColor(colour)

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex):
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

        self.table_widget = parent
        self.table_widget.setMouseTracking(True)
        self.table_widget.itemEntered.connect(lambda table_item: self.handle_item_entered(table_item))
        self.table_widget.itemExited.connect(lambda table_item: self.handle_item_exited(table_item))

        self.min = float(get_user_interface_property(item_type + "-min"))
        self.max = float(get_user_interface_property(item_type + "-max"))
        self.step = float(get_user_interface_property(item_type + "-step"))
        self.decimals = int(get_user_interface_property(item_type + "-dp"))

        self.hovered_row = -1

    def handle_item_entered(self, table_item: QTableWidgetItem) -> None:
        """Handles when a table item is hovered over."""
        self.hovered_row = table_item.row()
        self.table_widget.viewport().update()

    def handle_item_exited(self, _: QTableWidgetItem) -> None:
        """Handles when a table item is no longer hovered over."""
        self.hovered_row = -1

    def createEditor(self, parent: QWidget, style: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        """Overrides the parent method to create a custom QDoubleSpinBox."""
        box = QDoubleSpinBox(parent)
        box.setDecimals(self.decimals)

        box.setSingleStep(self.step)
        box.setMinimum(self.min)
        box.setMaximum(self.max)

        return box

    def paint(self, painter: QPainter, opt: QStyleOptionViewItem, index: QModelIndex) -> None:
        """Paints the table row colour when a hover event occurs."""
        option = QStyleOptionViewItem(opt)
        if index.row() == self.hovered_row:
            option.state |= QStyle.State_MouseOver
        super().paint(painter, option, index)


class StringItemDelegate(QStyledItemDelegate):
    """A class which creates a custom item delegate for managing string data stored in a QTableWidget."""

    def __init__(self, parent):
        """Initializes the item delegate using the properties stored in the user interface properties file."""
        super(StringItemDelegate, self).__init__(parent)

        self.table_widget = parent
        self.table_widget.setMouseTracking(True)
        self.table_widget.itemEntered.connect(lambda table_item: self.handle_item_entered(table_item))
        self.table_widget.itemExited.connect(lambda table_item: self.handle_item_exited(table_item))

        self.hovered_row = -1

    def handle_item_entered(self, table_item: QTableWidgetItem) -> None:
        """Handles when a table item is hovered over."""
        self.hovered_row = table_item.row()
        self.table_widget.viewport().update()

    def handle_item_exited(self, _: QTableWidgetItem) -> None:
        """Handles when a table item is no longer hovered over."""
        self.hovered_row = -1

    def paint(self, painter: QPainter, opt: QStyleOptionViewItem, index: QModelIndex) -> None:
        """Paints the table row colour when a hover event occurs."""
        option = QStyleOptionViewItem(opt)
        if index.row() == self.hovered_row:
            option.state |= QStyle.State_MouseOver
        super().paint(painter, option, index)
