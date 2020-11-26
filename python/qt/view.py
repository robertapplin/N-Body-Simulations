# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import qtawesome as qta

from n_body_simulations.body_data_table import BodyDataTableWidget, ColourTableWidget
from n_body_simulations.custom_actions import DoubleSpinBoxAction, LineEditButtonAction, SpinBoxButtonAction
from n_body_simulations.interactive_plot import InteractivePlot
from n_body_simulations.main_window_ui import Ui_MainWindow
from n_body_simulations.splitter_widgets import Splitter
from NBodySimulations import Vector2D

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QTableWidgetItem, QToolButton


class NBodySimulationsView(Ui_MainWindow, QObject):
    """A class used as a view for the main GUI (MVP)."""
    removeBodyClickedSignal = pyqtSignal()
    addBodyClickedSignal = pyqtSignal(str)
    addBodiesClickedSignal = pyqtSignal(int)
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
    bodyVelocityChangedSignal = pyqtSignal(str, float, float)

    def __init__(self, parent=None):
        """Initialize the view and perform basic setup of the widgets."""
        super(NBodySimulationsView, self).__init__()
        self.setupUi(parent)

        self.play_icon = None
        self.pause_icon = None

        self.add_single_body_action = None
        self.add_multiple_bodies_action = None
        self.time_step_action = None
        self.duration_action = None

        self.splitter = None
        self.plot_frame = None
        self.table_frame = None
        self.horizontal_layout = None
        self.colour_table = None
        self.body_data_table = None
        self.interactive_plot = None

        self.setup_icons()
        self.setup_splitter_widget()
        self.setup_table_widgets()
        self.setup_interactive_plot_widget()
        self.setup_add_body_widget()
        self.setup_time_settings_widget()

        self.pbRemoveBody.clicked.connect(self.emit_remove_body_clicked)
        self.pbInteractiveMode.clicked.connect(self.handle_interactive_mode_clicked)
        self.pbShowPositionLabels.clicked.connect(self.handle_show_position_labels_clicked)
        self.pbShowVelocityArrows.clicked.connect(self.handle_show_velocity_arrows_clicked)
        self.cbVelocityArrowMagnification.currentTextChanged.connect(lambda magnification:
                                                                     self.handle_velocity_magnification_changed(
                                                                         magnification))
        self.pbStop.clicked.connect(self.handle_stop_clicked)
        self.pbPlayPause.clicked.connect(self.emit_play_pause_clicked)
        self.colour_table.cellChanged.connect(lambda row, column: self.handle_body_colour_changed(row, column))
        self.body_data_table.cellClicked.connect(lambda row, column: self.handle_cell_clicked(row, column))
        self.body_data_table.cellChanged.connect(lambda row, column: self.handle_body_data_changed(row, column))
        self.add_single_body_action.push_button.clicked.connect(self.emit_add_body_clicked)
        self.add_multiple_bodies_action.push_button.clicked.connect(self.emit_add_bodies_clicked)
        self.time_step_action.double_spin_box.valueChanged.connect(lambda value: self.emit_time_step_changed(value))
        self.duration_action.double_spin_box.valueChanged.connect(lambda value: self.emit_duration_changed(value))

        self.interactive_plot.bodyMovedSignal.connect(lambda name, x, y: self.handle_body_moved(name, x, y))
        self.interactive_plot.bodyVelocityChangedSignal.connect(lambda name, vx, vy:
                                                                self.handle_body_velocity_changed(name, vx, vy))

        self._last_selected_body_name = None

    def setup_icons(self) -> None:
        """Setup the button icons."""
        self.play_icon = qta.icon('mdi.play', scale_factor=1.5, color='green')
        self.pause_icon = qta.icon('mdi.pause', scale_factor=1.5, color='blue')

        self.pbPlayPause.setIcon(self.play_icon)
        self.pbStop.setIcon(qta.icon('mdi.stop', scale_factor=1.5, color='red'))
        self.pbInteractiveMode.setIcon(qta.icon('mdi.gesture-tap', scale_factor=1.4))
        self.pbShowPositionLabels.setIcon(qta.icon('mdi.numeric', scale_factor=1.4))
        self.pbShowVelocityArrows.setIcon(qta.icon('mdi.arrow-top-right', scale_factor=1.2))
        self.tbTimeSettings.setIcon(qta.icon('mdi.timer', scale_factor=1.3))
        self.tbAddBody.setIcon(qta.icon('mdi.plus', scale_factor=1.5))
        self.pbRemoveBody.setIcon(qta.icon('mdi.minus', scale_factor=1.5))

    def setup_splitter_widget(self) -> None:
        """Setup the splitter widget."""
        self.splitter = Splitter(qta.icon('mdi.dots-horizontal', scale_factor=1.0))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setStyleSheet("QSplitter::handle { background-color: transparent; }")

        self.centralwidget.layout().addWidget(self.splitter)

        self.table_frame = QFrame()
        self.table_frame.setStyleSheet("QFrame { border: 1px solid #828790; }")
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        self.table_frame.setLayout(horizontal_layout)

        self.splitter.addWidget(self.table_frame)

    def setup_table_widgets(self) -> None:
        """Setup the table widgets."""
        self.colour_table = ColourTableWidget()
        self.table_frame.layout().addWidget(self.colour_table)

        self.body_data_table = BodyDataTableWidget()
        self.table_frame.layout().addWidget(self.body_data_table)

    def setup_interactive_plot_widget(self) -> None:
        """Setup the interactive plot widget."""
        self.plot_frame = QFrame()
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_frame.setLayout(grid_layout)
        self.plot_frame.setMinimumWidth(100)
        self.plot_frame.setMinimumHeight(100)

        self.interactive_plot = InteractivePlot()
        self.plot_frame.layout().addWidget(self.interactive_plot.canvas())

        self.splitter.addWidget(self.plot_frame)

    def setup_add_body_widget(self) -> None:
        """Setup the custom add body tool button widget."""
        self.add_single_body_action = LineEditButtonAction("Add Body", "[a-zA-Z][a-zA-Z0-9]*(?:[-])[a-zA-Z0-9]*")
        self.add_multiple_bodies_action = SpinBoxButtonAction("Add Bodies")

        self.tbAddBody.addAction(self.add_single_body_action)
        self.tbAddBody.addAction(self.add_multiple_bodies_action)
        self.tbAddBody.setPopupMode(QToolButton.InstantPopup)

    def setup_time_settings_widget(self) -> None:
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
        self.addBodyClickedSignal.emit(self.add_single_body_action.line_edit.text())
        self.add_single_body_action.line_edit.setText("")

    def emit_add_bodies_clicked(self) -> None:
        """Emit that the add bodies button was clicked."""
        self.addBodiesClickedSignal.emit(self.add_multiple_bodies_action.spin_box.value())
        self.add_multiple_bodies_action.spin_box.setValue(1)

    def emit_play_pause_clicked(self) -> None:
        """Emit that the play/pause button was clicked."""
        self.playPauseClickedSignal.emit()

    def emit_time_step_changed(self, value: float) -> None:
        """Emit that the time step was changed."""
        self.timeStepChangedSignal.emit(value)

    def emit_duration_changed(self, value: float) -> None:
        """Emit that the duration was changed."""
        self.durationChangedSignal.emit(value)

    def handle_cell_clicked(self, row_index: int, _: int) -> None:
        """Handle when a table row is selected."""
        self._last_selected_body_name = self._body_at_index(row_index)

    def handle_body_data_changed(self, row_index: int, column_index: int) -> None:
        """Handle when body data in the table is changed."""
        self.set_interactive_mode(True)

        table_signals = {self.body_data_table.mass_column.index: self.massChangedSignal,
                         self.body_data_table.x_column.index: self.xPositionChangedSignal,
                         self.body_data_table.y_column.index: self.yPositionChangedSignal,
                         self.body_data_table.vx_column.index: self.xVelocityChangedSignal,
                         self.body_data_table.vy_column.index: self.yVelocityChangedSignal}

        signal = table_signals.get(column_index, None)
        if signal is not None:
            signal.emit(self._body_at_index(row_index), self._get_cell_double(row_index, column_index))
        elif column_index == self.body_data_table.name_column.index:
            self.bodyNameChangedSignal.emit(self._last_selected_body_name, self._body_at_index(row_index))

    def handle_body_colour_changed(self, row_index: int, column_index: int) -> None:
        """Handles updating the colour of a body on the interactive plot when it is changed."""
        new_colour = self._get_cell_colour(row_index, column_index)
        self.interactive_plot.update_body_colour(self._body_at_index(row_index), new_colour)
        self.interactive_plot.draw()

    def handle_interactive_mode_clicked(self) -> None:
        """Handle when the interactive mode button is clicked."""
        self._show_position_labels_and_velocities(self.pbInteractiveMode.isChecked())

        self.set_as_playing(False)
        self.interactive_plot.disable_animation()
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def handle_show_position_labels_clicked(self) -> None:
        """Handle when the show position labels button is clicked."""
        self.interactive_plot.show_position_labels(self.pbShowPositionLabels.isChecked())
        self.interactive_plot.draw()

    def handle_show_velocity_arrows_clicked(self) -> None:
        """Handle when the show velocity arrows button is clicked."""
        self.interactive_plot.show_velocity_arrows(self.pbShowVelocityArrows.isChecked())
        self.interactive_plot.draw()

    def handle_velocity_magnification_changed(self, magnification: str) -> None:
        """Handles when the magnification of the velocity arrows is changed."""
        self.interactive_plot.set_velocity_arrow_magnification(int(magnification[1:]))
        self.interactive_plot.draw()

    def handle_stop_clicked(self) -> None:
        """Handle when the stop button is clicked."""
        self.set_interactive_mode(True)

    def handle_body_moved(self, body_name: str, x: float, y: float) -> None:
        """Handles when a body has been moved on the interactive plot."""
        self.body_data_table.blockSignals(True)

        row_index = self._index_of_body(body_name)
        self.body_data_table.setItem(row_index, self.body_data_table.x_column.index, self._create_table_double(x))
        self.body_data_table.setItem(row_index, self.body_data_table.y_column.index, self._create_table_double(y))

        self.body_data_table.blockSignals(False)

        self.bodyMovedSignal.emit(body_name, x, y)

    def handle_body_velocity_changed(self, body_name: str, vx: float, vy: float) -> None:
        """Handles when a bodies velocity has been changed on the interactive plot."""
        self.body_data_table.blockSignals(True)

        row_index = self._index_of_body(body_name)
        self.body_data_table.setItem(row_index, self.body_data_table.vx_column.index, self._create_table_double(vx))
        self.body_data_table.setItem(row_index, self.body_data_table.vy_column.index, self._create_table_double(vy))

        self.body_data_table.blockSignals(False)

        self.bodyVelocityChangedSignal.emit(body_name, vx, vy)

    def selected_bodies(self) -> list:
        """Returns the name of the bodies which are currently selected."""
        selected_indices = self._selected_row_indices()
        if selected_indices is not None:
            return [self._body_at_index(row_index) for row_index in selected_indices]
        return None

    def remove_body(self, body_name: str) -> None:
        """Removes the specified body from the view."""
        self.set_interactive_mode(True)

        row_index = self._index_of_body(body_name)

        self.colour_table.removeRow(row_index)
        self.body_data_table.removeRow(row_index)

        self.interactive_plot.remove_body(body_name)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def add_bodies(self, body_parameters: dict) -> None:
        """Adds a number of bodies to the view."""
        self.set_interactive_mode(True)

        for body_name, parameters in body_parameters.items():
            random_colour = self.colour_table.random_colour()
            self.add_body_to_table(body_name, parameters, random_colour)
            self.interactive_plot.add_body(body_name, parameters[1], parameters[2], random_colour)

        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def add_body(self, body_name: str, initial_data: tuple) -> None:
        """Adds a body to the view."""
        self.set_interactive_mode(True)

        random_colour = self.colour_table.random_colour()
        self.add_body_to_table(body_name, initial_data, random_colour)

        self.interactive_plot.add_body(body_name, initial_data[1], initial_data[2], random_colour)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def add_body_to_table(self, body_name: str, body_data: tuple, colour: str) -> None:
        """Adds the data of a body to the table of data."""
        self.colour_table.blockSignals(True)
        self.body_data_table.blockSignals(True)

        row_index = self.body_data_table.rowCount()
        body_table = self.body_data_table

        self.body_data_table.insertRow(row_index)
        self.colour_table.insertRow(row_index)
        self.body_data_table.setItem(row_index, body_table.name_column.index, QTableWidgetItem(body_name))
        self.body_data_table.setItem(row_index, body_table.mass_column.index, self._create_table_double(body_data[0]))
        self.body_data_table.setItem(row_index, body_table.x_column.index, self._create_table_double(body_data[1].x))
        self.body_data_table.setItem(row_index, body_table.y_column.index, self._create_table_double(body_data[1].y))
        self.body_data_table.setItem(row_index, body_table.vx_column.index, self._create_table_double(body_data[2].x))
        self.body_data_table.setItem(row_index, body_table.vy_column.index, self._create_table_double(body_data[2].y))
        self.colour_table.setItem(row_index, self.colour_table.colour_column.index, self._create_table_colour(colour))

        self.colour_table.blockSignals(False)
        self.body_data_table.blockSignals(False)

    def update_body_name(self, old_name: str, new_name: str) -> None:
        """Updates the name of a body in the interactive plot when it is changed."""
        self.interactive_plot.update_body_name(old_name, new_name)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def update_body_position(self, body_name: str, position: Vector2D) -> None:
        """Updates the position of a body in the interactive plot when it is changed."""
        self.interactive_plot.update_body_position(body_name, position)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def update_body_velocity(self, body_name: str, velocity: Vector2D) -> None:
        """Updates the velocity of a body in the interactive plot when it is changed."""
        self.interactive_plot.update_body_velocity(body_name, velocity)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def set_name(self, body_name: str) -> None:
        """Sets the name of a body in the table. Used to reset a bodies name when renaming it fails."""
        self.body_data_table.blockSignals(True)
        self.body_data_table.setItem(self._selected_row_indices()[0], self.body_data_table.name_column.index,
                                     QTableWidgetItem(body_name))
        self.body_data_table.blockSignals(False)

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
        self.colour_table.setEnabled(enable)
        self.body_data_table.setEnabled(enable)
        self.pbRemoveBody.setEnabled(enable)
        self.tbAddBody.setEnabled(enable)
        self.tbTimeSettings.setEnabled(enable)
        self.pbInteractiveMode.setEnabled(enable)
        self.pbStop.setEnabled(enable)
        self.pbPlayPause.setEnabled(enable)

    def start_simulation(self, simulation_results: tuple) -> None:
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
        self.interactive_plot.update_axes_limits(initial_data=False)
        self.interactive_plot.play_animation()

    def get_axes_limits(self) -> tuple:
        """Returns the axes limits currently being used for the interactive plot."""
        return self.interactive_plot.get_axes_limits()

    def _show_position_labels_and_velocities(self, show_visuals: bool) -> None:
        """Shows or hides the position labels and velocity arrows on the interactive plot."""
        self.interactive_plot.show_position_labels(show_visuals)
        self.pbShowPositionLabels.setChecked(show_visuals)
        self.interactive_plot.show_velocity_arrows(show_visuals)
        self.pbShowVelocityArrows.setChecked(show_visuals)

    @staticmethod
    def _create_table_double(value: float) -> QTableWidgetItem:
        """Creates a table item and sets its role."""
        item = QTableWidgetItem()
        item.setData(Qt.EditRole, value)
        return item

    @staticmethod
    def _create_table_colour(colour: str) -> QTableWidgetItem:
        """Creates a table item and sets its background colour role."""
        item = QTableWidgetItem()
        item.setData(Qt.BackgroundRole, QColor(colour))
        return item

    def _get_cell_double(self, row_index: int, column_index: int) -> float:
        """Gets the float value of a table item."""
        return float(self.body_data_table.item(row_index, column_index).text())

    def _get_cell_colour(self, row_index: int, column_index: int) -> str:
        """Gets the background colour of a table item in string format."""
        return self.colour_table.item(row_index, column_index).background().color().name()

    def _body_at_index(self, row_index: int) -> str:
        """Returns the name of the body at a given row index."""
        return self.body_data_table.item(row_index, self.body_data_table.name_column.index).text()

    def _index_of_body(self, body_name: str) -> int:
        """Returns the row index of a given body."""
        for row_index in range(self.body_data_table.rowCount()):
            if self.body_data_table.item(row_index, self.body_data_table.name_column.index).text() == body_name:
                return row_index
        return -1

    def _selected_row_indices(self) -> list:
        """Returns the indices of the selected row."""
        selection_model = self.body_data_table.selectionModel()
        if selection_model.hasSelection():
            return sorted([model_index.row() for model_index in selection_model.selectedRows()], reverse=True)
        return None
