# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import qtawesome as qta

from n_body_simulations.add_body_dialog import AddBodyDialog
from n_body_simulations.double_spinbox_action import DoubleSpinBoxAction
from n_body_simulations.interactive_plot import InteractivePlot
from n_body_simulations.main_window_ui import Ui_MainWindow
from n_body_simulations.table_item_delegate import TableItemDelegate
from n_body_simulations.xml_reader import get_user_interface_property
from NBodySimulations import Vector2D

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QTableWidgetItem, QToolButton


class TableColumn:
    """A class used to store the details of a column in the data table."""

    def __init__(self, index: int, header: str, unit: str = None):
        """Initialize the column details."""
        self.index = index
        self.header = header
        if unit is not None:
            self.header += " (" + unit + ")"


class NBodySimulationsView(Ui_MainWindow, QObject):
    """A class used as a view for the main GUI (MVP)."""
    removeBodyClickedSignal = pyqtSignal()
    addBodyClickedSignal = pyqtSignal()
    bodyNameChangedSignal = pyqtSignal(str, str)
    massChangedSignal = pyqtSignal(str, float)
    xPositionChangedSignal = pyqtSignal(str, float)
    yPositionChangedSignal = pyqtSignal(str, float)
    xVelocityChangedSignal = pyqtSignal(str, float)
    yVelocityChangedSignal = pyqtSignal(str, float)
    timeStepChangedSignal = pyqtSignal(float)
    durationChangedSignal = pyqtSignal(float)
    playPauseClickedSignal = pyqtSignal()

    bodyMovedSignal = pyqtSignal(str, float, float)

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
        """Initialize the view and perform basic setup of the widgets."""
        super(NBodySimulationsView, self).__init__()
        self.setupUi(parent)

        self.play_icon = None
        self.pause_icon = None

        self.time_step_action = None
        self.duration_action = None

        self.setup_icons()
        self.setup_table_widget()
        self.setup_time_settings_widget()

        self.interactive_plot = InteractivePlot()
        self.plotLayout.addWidget(self.interactive_plot.canvas())

        self.pbRemoveBody.clicked.connect(self.emit_remove_body_clicked)
        self.pbAddBody.clicked.connect(self.emit_add_body_clicked)
        self.pbInteractiveMode.clicked.connect(self.handle_interactive_mode_clicked)
        self.pbStop.clicked.connect(self.handle_stop_clicked)
        self.pbPlayPause.clicked.connect(self.emit_play_pause_clicked)
        self.twBodyData.cellClicked.connect(lambda row, column: self.handle_cell_clicked(row, column))
        self.twBodyData.cellChanged.connect(lambda row, column: self.handle_body_data_changed(row, column))
        self.time_step_action.double_spin_box.valueChanged.connect(lambda value: self.emit_time_step_changed(value))
        self.duration_action.double_spin_box.valueChanged.connect(lambda value: self.emit_duration_changed(value))

        self.interactive_plot.bodyMovedSignal.connect(lambda name, x, y: self.handle_body_moved(name, x, y))

        self._selected_body = None

    def setup_icons(self) -> None:
        """Setup the button icons."""
        self.play_icon = qta.icon('mdi.play', scale_factor=1.5, color='green')
        self.pause_icon = qta.icon('mdi.pause', scale_factor=1.5, color='blue')

        self.pbPlayPause.setIcon(self.play_icon)
        self.pbStop.setIcon(qta.icon('mdi.stop', scale_factor=1.5, color='red'))
        self.pbInteractiveMode.setIcon(qta.icon('mdi.gesture-tap', scale_factor=1.4))
        self.tbTimeSettings.setIcon(qta.icon('mdi.timer', scale_factor=1.3))
        self.pbAddBody.setIcon(qta.icon('mdi.plus', scale_factor=1.5))
        self.pbRemoveBody.setIcon(qta.icon('mdi.minus', scale_factor=1.5))

    def setup_table_widget(self) -> None:
        """Setup the table widget."""
        self.twBodyData.setHorizontalHeaderLabels([self.name_column.header, self.mass_column.header,
                                                   self.x_column.header, self.y_column.header,
                                                   self.vx_column.header, self.vy_column.header])

        mass_item_delegate = TableItemDelegate(self.twBodyData, TableItemDelegate.Mass)
        position_item_delegate = TableItemDelegate(self.twBodyData, TableItemDelegate.Position)
        velocity_item_delegate = TableItemDelegate(self.twBodyData, TableItemDelegate.Velocity)

        self.twBodyData.setItemDelegateForColumn(self.mass_column.index, mass_item_delegate)
        self.twBodyData.setItemDelegateForColumn(self.x_column.index, position_item_delegate)
        self.twBodyData.setItemDelegateForColumn(self.y_column.index, position_item_delegate)
        self.twBodyData.setItemDelegateForColumn(self.vx_column.index, velocity_item_delegate)
        self.twBodyData.setItemDelegateForColumn(self.vy_column.index, velocity_item_delegate)

    def setup_time_settings_widget(self):
        """Setup the custom time settings widget."""
        self.time_step_action = DoubleSpinBoxAction("Time Step: ", DoubleSpinBoxAction.TimeStep)
        self.duration_action = DoubleSpinBoxAction("Duration: ", DoubleSpinBoxAction.Duration)

        self.tbTimeSettings.addAction(self.time_step_action)
        self.tbTimeSettings.addAction(self.duration_action)
        self.tbTimeSettings.setPopupMode(QToolButton.InstantPopup)

    def emit_remove_body_clicked(self) -> None:
        """Emit that the remove body button was clicked."""
        self.removeBodyClickedSignal.emit()

    def emit_add_body_clicked(self) -> None:
        """Emit that the add body button was clicked."""
        self.addBodyClickedSignal.emit()

    def emit_play_pause_clicked(self) -> None:
        """Emit that the play/pause button was clicked."""
        self.playPauseClickedSignal.emit()

    def emit_time_step_changed(self, value: float) -> None:
        """Emit that the time step was changed."""
        self.timeStepChangedSignal.emit(value)

    def emit_duration_changed(self, value: float) -> None:
        """Emit that the duration was changed."""
        self.durationChangedSignal.emit(value)

    def handle_cell_clicked(self, row_index: int, column_index: int) -> None:
        """Handle when a table row is selected."""
        self._selected_body = self._body_at_index(row_index)

    def handle_body_data_changed(self, row_index: int, column_index: int) -> None:
        """Handle when body data in the table is changed."""
        self.set_interactive_mode(True)

        table_signals = {self.mass_column.index: self.massChangedSignal,
                         self.x_column.index: self.xPositionChangedSignal,
                         self.y_column.index: self.yPositionChangedSignal,
                         self.vx_column.index: self.xVelocityChangedSignal,
                         self.vy_column.index: self.yVelocityChangedSignal}

        signal = table_signals.get(column_index, None)
        if signal is not None:
            signal.emit(self._selected_body, self._get_table_value(row_index, column_index))
        else:
            self.bodyNameChangedSignal.emit(self._selected_body, self._body_at_index(row_index))

    def handle_interactive_mode_clicked(self) -> None:
        """Handle when the interactive mode button is clicked."""
        self.set_as_playing(False)
        self.interactive_plot.disable_animation()

    def handle_stop_clicked(self) -> None:
        """Handle when the stop button is clicked."""
        self.set_interactive_mode(True)

    def handle_body_moved(self, body_name: str, x: float, y: float) -> None:
        """Handles when a body has been moved on the interactive plot."""
        self.twBodyData.blockSignals(True)

        row_index = self._index_of_body(body_name)
        self.twBodyData.setItem(row_index, self.x_column.index, self._create_table_value(x))
        self.twBodyData.setItem(row_index, self.y_column.index, self._create_table_value(y))

        self.twBodyData.blockSignals(False)

        self.bodyMovedSignal.emit(body_name, x, y)

    def clear(self) -> None:
        """Clear all data displayed in the view."""
        self.interactive_plot.clear()
        self.twBodyData.clearContents()

    def reset_view(self, bodies: dict, time_step: float, duration: float) -> None:
        """Clear the view, and then add some bodies to the view."""
        self.clear()
        self.add_bodies(bodies)
        self.set_time_step(time_step)
        self.set_duration(duration)

    def selected_body(self) -> str:
        """Returns the name of the body which is currently selected."""
        selected_index = self._selected_row_index()
        if selected_index != -1:
            return self._body_at_index(selected_index)
        return None

    def remove_body(self, body_name: str) -> None:
        """Removes the specified body from the view."""
        self.set_interactive_mode(True)

        self.twBodyData.removeRow(self._selected_row_index())

        self.interactive_plot.remove_body(body_name)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def add_bodies(self, body_parameters: dict) -> None:
        """Adds a number of bodies to the view."""
        self.set_interactive_mode(True)

        for body_name, parameters in body_parameters.items():
            self.add_body_to_table(body_name, parameters)
            self.interactive_plot.add_body(body_name, parameters[1])

        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def add_body(self, body_name: str, initial_data: tuple) -> None:
        """Adds a body to the view."""
        self.set_interactive_mode(True)

        self.add_body_to_table(body_name, initial_data)

        self.interactive_plot.add_body(body_name, initial_data[1])
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def add_body_to_table(self, body_name: str, body_data: tuple) -> None:
        """Adds the data of a body to the table of data."""
        self.twBodyData.blockSignals(True)
        row_index = self.twBodyData.rowCount()

        self.twBodyData.insertRow(row_index)
        self.twBodyData.setItem(row_index, self.name_column.index, QTableWidgetItem(body_name))
        self.twBodyData.setItem(row_index, self.mass_column.index, self._create_table_value(body_data[0]))
        self.twBodyData.setItem(row_index, self.x_column.index, self._create_table_value(body_data[1].x))
        self.twBodyData.setItem(row_index, self.y_column.index, self._create_table_value(body_data[1].y))
        self.twBodyData.setItem(row_index, self.vx_column.index, self._create_table_value(body_data[2].x))
        self.twBodyData.setItem(row_index, self.vy_column.index, self._create_table_value(body_data[2].y))
        self.twBodyData.blockSignals(False)

    def update_body_name(self, old_name: str, new_name: str) -> None:
        """Updates the name of a body in the interactive plot when it is changed."""
        self.interactive_plot.update_body_name(old_name, new_name)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def update_body_position(self, body_name: str, position: Vector2D) -> None:
        """Updates the position of a body in the interactive plot when it is changed."""
        self.interactive_plot.remove_body(body_name)
        self.interactive_plot.add_body(body_name, position)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def set_name(self, body_name: str) -> None:
        """Sets the name of a body in the table. Used to reset a bodies name when renaming it fails."""
        self.twBodyData.blockSignals(True)
        self.twBodyData.setItem(self._selected_row_index(), self.name_column.index, QTableWidgetItem(body_name))
        self.twBodyData.blockSignals(False)

    def set_time_step(self, time_step: float) -> None:
        """Sets the time step shown in the view."""
        self.time_step_action.double_spin_box.blockSignals(True)
        self.time_step_action.double_spin_box.setValue(time_step)
        self.time_step_action.double_spin_box.blockSignals(False)

    def set_duration(self, duration: float) -> None:
        """Sets the duration shown in the view."""
        self.time_step_action.double_spin_box.blockSignals(True)
        self.duration_action.double_spin_box.setValue(duration)
        self.time_step_action.double_spin_box.blockSignals(False)

    def set_interactive_mode(self, interactive_mode: bool) -> None:
        """Sets the view to be in interactive mode. This is required to prevent interference from the animator."""
        self.pbInteractiveMode.setChecked(interactive_mode)
        if interactive_mode:
            self.handle_interactive_mode_clicked()

    def set_as_playing(self, playing: bool) -> None:
        """Sets the current role of the play/pause button."""
        self.pbPlayPause.setToolTip("Pause" if playing else "Play")
        self.pbPlayPause.setIcon(self.pause_icon if playing else self.play_icon)
        if playing:
            self.set_interactive_mode(False)

    def is_simulating(self) -> bool:
        """Returns true if a simulation is currently being animated."""
        return self.pbPlayPause.toolTip() != "Play"

    def enable_view(self, enable: bool) -> None:
        """Enables or disables the widgets seen in the view."""
        self.twBodyData.setEnabled(enable)
        self.pbRemoveBody.setEnabled(enable)
        self.pbAddBody.setEnabled(enable)
        self.tbTimeSettings.setEnabled(enable)
        self.pbInteractiveMode.setEnabled(enable)
        self.pbStop.setEnabled(enable)
        self.pbPlayPause.setEnabled(enable)

    @staticmethod
    def open_add_body_dialog() -> tuple:
        """Opens the dialog used for adding a body to the simulation."""
        dialog = AddBodyDialog()
        dialog.exec_()
        return dialog.new_body_data()

    def start_simulation(self, simulation_results: dict) -> None:
        """Starts animating the results of a simulation."""
        self.interactive_plot.set_simulation_data(simulation_results)
        self.interactive_plot.update_axes_limits(initial_data=False)
        self.interactive_plot.start_animation()

    def stop_simulation(self) -> None:
        """Stops the animation of a simulation."""
        self.interactive_plot.stop_animation()

    def pause_simulation(self) -> None:
        """Pauses the animation of a simulation."""
        self.interactive_plot.pause_animation()

    def play_simulation(self) -> None:
        """Plays the animation of a simulation."""
        self.interactive_plot.play_animation()

    @staticmethod
    def _create_table_value(value: float) -> QTableWidgetItem:
        """Creates a table item and sets its role."""
        item = QTableWidgetItem()
        item.setData(Qt.EditRole, value)
        return item

    def _get_table_value(self, row_index: int, column_index: int) -> float:
        """Gets the float value of a table item."""
        return float(self.twBodyData.item(row_index, column_index).text())

    def _body_at_index(self, row_index: int) -> str:
        """Returns the name of the body at a given row index."""
        return self.twBodyData.item(row_index, 0).text()

    def _index_of_body(self, body_name: str) -> int:
        """Returns the row index of a given body."""
        for row_index in range(self.twBodyData.rowCount()):
            if self.twBodyData.item(row_index, self.name_column.index).text() == body_name:
                return row_index
        return -1

    def _selected_row_index(self) -> int:
        """Returns the index of the selected row."""
        selection_model = self.twBodyData.selectionModel()
        if selection_model.hasSelection():
            return selection_model.currentIndex().row()
        return -1
