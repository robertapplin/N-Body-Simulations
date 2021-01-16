# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.table_item_delegates import ColourItemDelegate, DoubleItemDelegate, StringItemDelegate
from n_body_simulations.xml_reader import get_user_interface_property

from PyQt5.QtCore import pyqtSignal, QEvent, QModelIndex, QObject, QPersistentModelIndex, Qt
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem


class TableColumn:
    """A class used to store the details of a column in the data table."""

    def __init__(self, index: int, header: str, unit: str = None):
        """Initialize the column details."""
        self.index = index
        self.header = header
        if unit is not None:
            self.header += " (" + unit + ")"


class BodyDataTableWidget(QTableWidget):
    """A class derived from a QTableWidget to store body data."""
    itemExited = pyqtSignal(QTableWidgetItem)

    time_unit = get_user_interface_property("time-unit")
    mass_unit = get_user_interface_property("mass-unit")
    position_unit = get_user_interface_property("position-unit")
    velocity_unit = position_unit + "/" + time_unit

    name_column = TableColumn(0, "Name")
    mass_column = TableColumn(1, "Mass", mass_unit)
    x_column = TableColumn(2, "X", position_unit)
    y_column = TableColumn(3, "Y", position_unit)
    vx_column = TableColumn(4, "Vx", velocity_unit)
    vy_column = TableColumn(5, "Vy", velocity_unit)

    def __init__(self, parent=None):
        """Initialize the table widget for storing body data."""
        super(BodyDataTableWidget, self).__init__(parent)

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setShowGrid(False)
        self.setColumnCount(6)
        self.setRowCount(0)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setColumnWidth(5, 1)
        self.setStyleSheet("QHeaderView::section {\n"
                           "    font-size: 10pt;\n"
                           "    background-color: #f0f0f0;\n"
                           "    padding: 2px;\n"
                           "    border: 1px solid #828790;\n"
                           "    border-top: 0px;"
                           "    border-right: 0px;"
                           "}\n"
                           "\n"
                           "QTableWidget {\n"
                           "    font-size: 8pt;\n"
                           "    border: 1px solid #828790;\n"
                           "}\n"
                           "\n"
                           "QTableWidget::item:selected {\n"
                           "    background-color: #c7e0ff;\n"
                           "    color: #000000;\n"
                           "}"
                           "\n"
                           "QTableWidget::item:hover {\n"
                           "    background-color: #c7e0ff;\n"
                           "    color: #000000;\n"
                           "}"
                           "\n"
                           "QFrame {\n"
                           "    border: none;\n"
                           "}")

        self._last_index = QPersistentModelIndex()
        self.viewport().installEventFilter(self)

        self.setup_table()

    def setup_table(self) -> None:
        """Setup the table widget."""
        self.setHorizontalHeaderLabels([self.name_column.header, self.mass_column.header, self.x_column.header,
                                        self.y_column.header, self.vx_column.header, self.vy_column.header])

        name_item_delegate = StringItemDelegate(self)
        mass_item_delegate = DoubleItemDelegate(self, DoubleItemDelegate.Mass)
        position_item_delegate = DoubleItemDelegate(self, DoubleItemDelegate.Position)
        velocity_item_delegate = DoubleItemDelegate(self, DoubleItemDelegate.Velocity)

        self.setItemDelegateForColumn(self.name_column.index, name_item_delegate)
        self.setItemDelegateForColumn(self.mass_column.index, mass_item_delegate)
        self.setItemDelegateForColumn(self.x_column.index, position_item_delegate)
        self.setItemDelegateForColumn(self.y_column.index, position_item_delegate)
        self.setItemDelegateForColumn(self.vx_column.index, velocity_item_delegate)
        self.setItemDelegateForColumn(self.vy_column.index, velocity_item_delegate)

    def eventFilter(self, widget: QObject, event: QEvent) -> bool:
        """Emits a signal when a table cell is exited."""
        if widget is self.viewport():
            index = self._last_index
            if event.type() == QEvent.MouseMove:
                index = self.indexAt(event.pos())
            elif event.type() == QEvent.Leave:
                index = QModelIndex()
            if index != self._last_index:
                item = self.item(self._last_index.row(), self._last_index.column())
                if item is not None:
                    self.itemExited.emit(item)
                self._last_index = QPersistentModelIndex(index)
        return QTableWidget.eventFilter(self, widget, event)


class ColourTableWidget(QTableWidget):
    """A class derived from a QTableWidget to display body colours."""
    colour_column = TableColumn(0, "")

    def __init__(self, parent=None):
        """Initialize the table widget for displaying body colours."""
        super(ColourTableWidget, self).__init__(parent)

        self.setMinimumWidth(30)
        self.setMaximumWidth(30)
        self.setShowGrid(False)
        self.setColumnCount(1)
        self.setRowCount(0)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("QHeaderView::section {\n"
                           "    font-size: 10pt;\n"
                           "    background-color: #f0f0f0;\n"
                           "    padding: 2px;\n"
                           "    border: 1px solid #828790;\n"
                           "    border-top: 0px;"
                           "    border-left: 0px;"
                           "}\n"
                           "\n"
                           "QFrame {\n"
                           "    border: none;\n"
                           "}")

        colour_item_delegate = ColourItemDelegate(self)
        self.setItemDelegateForColumn(self.colour_column.index, colour_item_delegate)
