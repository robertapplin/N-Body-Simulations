# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import qtawesome as qta

from enum import Enum

from n_body_simulations.plotting.interactive_plot import InteractivePlot
from n_body_simulations.qt.body_data_table import BodyDataTableWidget, ColourTableWidget
from n_body_simulations.qt.custom_actions import (AnimationFrameDelayAction, DoubleSpinBoxAction, LineEditButtonAction,
                                                  PositionPlotOptionsAction, SpinBoxButtonAction,
                                                  VelocityPlotOptionsAction)
from n_body_simulations.qt.splitter_widgets import Splitter
from n_body_simulations.qt.ui.main_window_ui import Ui_NBodySimulator
from NBodySimulations import Vector2D

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog, QFrame, QGridLayout, QHBoxLayout, QTableWidgetItem, QToolButton, QWidget

FILENAME_FILTERS = ["Text files (*.txt)"]


class NBodySimulationsView(Ui_NBodySimulator, QWidget):
    """A class used as a view for the NBodySimulator (MVP)."""
    class ViewEvent(Enum):
        LoadProjectClicked = 1
        SaveProjectClicked = 2
        RemoveBodyClicked = 3
        AddBodyClicked = 4
        AddBodiesClicked = 5
        TimeStepChanged = 6
        DurationChanged = 7
        NameChanged = 8
        MassChanged = 9
        XPositionChanged = 10
        YPositionChanged = 11
        VxPositionChanged = 12
        VyPositionChanged = 13
        PlayPauseClicked = 14
        BodyMovedOnPlot = 15
        BodyVelocityChangedOnPlot = 16

    def __init__(self, parent=None):
        """Initialize the view and perform basic setup of the widgets."""
        super(NBodySimulationsView, self).__init__(parent)
        self.setupUi(self)

        self.play_icon = None
        self.pause_icon = None

        self.add_single_body_action = None
        self.add_multiple_bodies_action = None
        self.time_step_action = None
        self.duration_action = None
        self.animation_frame_delay_action = None
        self.position_plot_options_action = None
        self.velocity_plot_options_action = None

        self.splitter = None
        self.plot_frame = None
        self.table_frame = None
        self.horizontal_layout = None
        self.colour_table = None
        self.body_data_table = None
        self.interactive_plot = None

        self.presenter = None

        self.setup_icons()
        self.setup_splitter_widget()
        self.setup_table_widgets()
        self.setup_interactive_plot_widget()
        self.setup_add_body_widget()
        self.setup_time_settings_widget()
        self.setup_plot_options_widget()

        self.pbLoadProject.clicked.connect(self.on_load_project_clicked)
        self.pbSaveProject.clicked.connect(self.on_save_project_clicked)
        self.pbRemoveBody.clicked.connect(self.on_remove_body_clicked)
        self.add_single_body_action.push_button.clicked.connect(self.on_add_body_clicked)
        self.add_multiple_bodies_action.push_button.clicked.connect(self.on_add_bodies_clicked)
        self.time_step_action.double_spin_box.valueChanged.connect(lambda value: self.on_time_step_changed(value))
        self.duration_action.double_spin_box.valueChanged.connect(lambda value: self.on_duration_changed(value))
        self.animation_frame_delay_action.delay_slider.valueChanged.connect(
            lambda value: self.on_animation_frame_delay_changed(value))
        self.position_plot_options_action.show_labels_button.clicked.connect(self.on_show_position_labels_clicked)
        self.velocity_plot_options_action.show_arrows_button.clicked.connect(self.on_show_velocity_arrows_clicked)
        self.velocity_plot_options_action.arrow_magnification.currentTextChanged.connect(
            lambda factor: self.on_velocity_magnification_changed(factor))
        self.colour_table.cellChanged.connect(lambda row, column: self.on_body_colour_changed(row, column))
        self.body_data_table.cellChanged.connect(lambda row, column: self.on_body_data_changed(row, column))
        self.pbInteractiveMode.clicked.connect(self.on_interactive_mode_clicked)
        self.pbStop.clicked.connect(self.on_stop_clicked)
        self.pbPlayPause.clicked.connect(self.on_play_pause_clicked)
        self.body_data_table.cellClicked.connect(lambda row, column: self.on_cell_clicked(row, column))

        self.interactive_plot.bodyMovedSignal.connect(lambda name, x, y: self.on_body_moved(name, x, y))
        self.interactive_plot.bodyVelocityChangedSignal.connect(lambda name, vx, vy:
                                                                self.on_body_velocity_changed(name, vx, vy))

        self._last_selected_body_name = None

    def setup_icons(self) -> None:
        """Setup the button icons."""
        self.play_icon = qta.icon('mdi.play', scale_factor=1.5, color='green')
        self.pause_icon = qta.icon('mdi.pause', scale_factor=1.5, color='blue')

        self.pbLoadProject.setIcon(qta.icon('mdi.file-download', scale_factor=1.3))
        self.pbSaveProject.setIcon(qta.icon('mdi.content-save', scale_factor=1.3))
        self.pbRemoveBody.setIcon(qta.icon('mdi.minus', scale_factor=1.5))
        self.tbAddBody.setIcon(qta.icon('mdi.plus', scale_factor=1.5))
        self.tbTimeSettings.setIcon(qta.icon('mdi.timer', scale_factor=1.3))
        self.tbPlotOptions.setIcon(qta.icon('mdi.chart-scatter-plot', scale_factor=1.2))
        self.pbInteractiveMode.setIcon(qta.icon('mdi.gesture-tap', scale_factor=1.4))
        self.pbStop.setIcon(qta.icon('mdi.stop', scale_factor=1.5, color='red'))
        self.pbPlayPause.setIcon(self.play_icon)

    def setup_splitter_widget(self) -> None:
        """Setup the splitter widget."""
        self.splitter = Splitter(qta.icon('mdi.dots-horizontal', scale_factor=1.0))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setStyleSheet("QSplitter::handle { background-color: transparent; }")

        self.layout().addWidget(self.splitter)

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

    def setup_plot_options_widget(self) -> None:
        """Setup the custom plot options widget."""
        self.animation_frame_delay_action = AnimationFrameDelayAction()
        self.position_plot_options_action = PositionPlotOptionsAction()
        self.velocity_plot_options_action = VelocityPlotOptionsAction()

        self.tbPlotOptions.addAction(self.animation_frame_delay_action)
        self.tbPlotOptions.addAction(self.position_plot_options_action)
        self.tbPlotOptions.addAction(self.velocity_plot_options_action)
        self.tbPlotOptions.setPopupMode(QToolButton.InstantPopup)

    def subscribe_presenter(self, presenter) -> None:
        """Subscribe the presenter for event notifications."""
        self.presenter = presenter

    def clear(self) -> None:
        """Clear all the data from the view."""
        self.colour_table.blockSignals(True)
        self.body_data_table.blockSignals(True)

        self.interactive_plot.clear()
        self.colour_table.setRowCount(0)
        self.body_data_table.setRowCount(0)

        self.colour_table.blockSignals(False)
        self.body_data_table.blockSignals(False)

    def on_load_project_clicked(self) -> None:
        """Notify presenter that the load project button was clicked."""
        self.presenter.notify_presenter(self.ViewEvent.LoadProjectClicked)

    def on_save_project_clicked(self) -> None:
        """Notify presenter that the save project button was clicked."""
        self.presenter.notify_presenter(self.ViewEvent.SaveProjectClicked)

    def on_remove_body_clicked(self) -> None:
        """Notify presenter that the remove body button was clicked."""
        self.presenter.notify_presenter(self.ViewEvent.RemoveBodyClicked)

    def on_add_body_clicked(self) -> None:
        """Notify presenter that the add body button was clicked."""
        self.presenter.notify_presenter(self.ViewEvent.AddBodyClicked, self.add_single_body_action.line_edit.text())
        self.add_single_body_action.line_edit.setText("")

    def on_add_bodies_clicked(self) -> None:
        """Notify presenter that the add bodies button was clicked."""
        self.presenter.notify_presenter(self.ViewEvent.AddBodiesClicked,
                                        self.add_multiple_bodies_action.spin_box.value())
        self.add_multiple_bodies_action.spin_box.setValue(1)

    def on_time_step_changed(self, value: float) -> None:
        """Notify presenter that the time step was changed."""
        self.presenter.notify_presenter(self.ViewEvent.TimeStepChanged, value)

    def on_duration_changed(self, value: float) -> None:
        """Notify presenter that the duration was changed."""
        self.presenter.notify_presenter(self.ViewEvent.DurationChanged, value)

    def on_body_colour_changed(self, row_index: int, column_index: int) -> None:
        """Handles updating the colour of a body on the interactive plot when it is changed."""
        new_colour = self._get_cell_colour(row_index, column_index)
        self.interactive_plot.update_body_colour(self._body_at_index(row_index), new_colour)
        self.interactive_plot.draw()

    def on_body_data_changed(self, row_index: int, column_index: int) -> None:
        """Notify presenter when body data in the table is changed."""
        self.set_interactive_mode(True)

        table_events = {self.body_data_table.mass_column.index: self.ViewEvent.MassChanged,
                        self.body_data_table.x_column.index: self.ViewEvent.XPositionChanged,
                        self.body_data_table.y_column.index: self.ViewEvent.YPositionChanged,
                        self.body_data_table.vx_column.index: self.ViewEvent.VxPositionChanged,
                        self.body_data_table.vy_column.index: self.ViewEvent.VyPositionChanged}

        event = table_events.get(column_index, None)
        if event is not None:
            self.presenter.notify_presenter(event, self._body_at_index(row_index),
                                            self._get_cell_double(row_index, column_index))
        elif column_index == self.body_data_table.name_column.index:
            self.presenter.notify_presenter(self.ViewEvent.NameChanged, self._last_selected_body_name,
                                            self._body_at_index(row_index))

    def on_velocity_magnification_changed(self, magnification: str) -> None:
        """Handles when the magnification of the velocity arrows is changed."""
        self.interactive_plot.set_velocity_arrow_magnification(int(magnification[1:]))
        self.interactive_plot.draw()

    def on_animation_frame_delay_changed(self, value: int) -> None:
        """Handles when the frame delay of the animation is changed."""
        self.set_interactive_mode(True)
        self.animation_frame_delay_action.delay_slider.setToolTip(f"Animation frame delay in milliseconds. "
                                                                  f"Current delay is {value} ms.")
        self.animation_frame_delay_action.delay_label.setText(f"{value} ms")
        self.interactive_plot.set_animation_interval(value)

    def on_show_position_labels_clicked(self) -> None:
        """Handle when the show position labels button is clicked."""
        showing_labels = self.position_plot_options_action.showing_position_labels()
        self.position_plot_options_action.set_is_showing_labels(showing_labels)

        self.interactive_plot.show_position_labels(showing_labels)
        self.interactive_plot.draw()

    def on_show_velocity_arrows_clicked(self) -> None:
        """Handle when the show velocity arrows button is clicked."""
        showing_arrows = self.velocity_plot_options_action.showing_velocity_arrows()
        self.velocity_plot_options_action.set_is_showing_arrows(showing_arrows)

        self.interactive_plot.show_velocity_arrows(showing_arrows)
        self.interactive_plot.draw()

    def on_interactive_mode_clicked(self) -> None:
        """Handle when the interactive mode button is clicked."""
        self.set_as_playing(False)
        self.interactive_plot.disable_animation()
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def on_stop_clicked(self) -> None:
        """Handle when the stop button is clicked."""
        self.set_interactive_mode(True)

    def on_play_pause_clicked(self) -> None:
        """Notify presenter that the play/pause button was clicked."""
        self.presenter.notify_presenter(self.ViewEvent.PlayPauseClicked)

    def on_cell_clicked(self, row_index: int, _: int) -> None:
        """Handle when a table row is selected."""
        self._last_selected_body_name = self._body_at_index(row_index)

    def on_body_moved(self, body_name: str, x: float, y: float) -> None:
        """Handles when a body has been moved on the interactive plot."""
        self.body_data_table.blockSignals(True)

        row_index = self._index_of_body(body_name)
        self.body_data_table.setItem(row_index, self.body_data_table.x_column.index, self._create_table_double(x))
        self.body_data_table.setItem(row_index, self.body_data_table.y_column.index, self._create_table_double(y))

        self.body_data_table.blockSignals(False)

        self.presenter.notify_presenter(self.ViewEvent.BodyMovedOnPlot, body_name, x, y)

    def on_body_velocity_changed(self, body_name: str, vx: float, vy: float) -> None:
        """Handles when a bodies velocity has been changed on the interactive plot."""
        self.body_data_table.blockSignals(True)

        row_index = self._index_of_body(body_name)
        self.body_data_table.setItem(row_index, self.body_data_table.vx_column.index, self._create_table_double(vx))
        self.body_data_table.setItem(row_index, self.body_data_table.vy_column.index, self._create_table_double(vy))

        self.body_data_table.blockSignals(False)

        self.presenter.notify_presenter(self.ViewEvent.BodyVelocityChangedOnPlot, body_name, vx, vy)

    @staticmethod
    def open_file_dialog_for_loading() -> str:
        """Opens a QFileDialog to get a file name for loading data."""
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilters(FILENAME_FILTERS)

        if dialog.exec_():
            return dialog.selectedFiles()[0]
        return None

    @staticmethod
    def open_file_dialog_for_saving() -> str:
        """Opens a QFileDialog to get a file name for saving data."""
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilters(FILENAME_FILTERS)

        if dialog.exec_():
            return dialog.selectedFiles()[0]
        return None

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

    def add_body(self, colour: str, body_name: str, initial_data: tuple) -> None:
        """Adds a body to the view."""
        self.set_interactive_mode(True)

        self.add_body_to_table(body_name, initial_data, colour)

        self.interactive_plot.add_body(colour, body_name, initial_data[0], initial_data[1], initial_data[2],
                                       not self.position_plot_options_action.showing_position_labels(),
                                       not self.velocity_plot_options_action.showing_velocity_arrows(),
                                       int(self.velocity_plot_options_action.arrow_magnification.currentText()[1:]))
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

    def update_body_mass(self, body_name: str, mass: float) -> None:
        """Updates the mass of a body in the interactive plot when it is changed."""
        self.interactive_plot.update_body_mass(body_name, mass)
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
            self.on_interactive_mode_clicked()

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
        self.tbPlotOptions.setEnabled(enable)
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

    def get_body_colour(self, body_name: str) -> str:
        """Returns the colour of a body."""
        return self.interactive_plot.get_body_colour(body_name)

    def get_axes_limits(self) -> tuple:
        """Returns the axes limits currently being used for the interactive plot."""
        return self.interactive_plot.get_axes_limits()

    def reset_plot_options(self) -> None:
        """Resets the plot options to their default states."""
        self.position_plot_options_action.set_is_showing_labels(True)
        self.velocity_plot_options_action.set_is_showing_arrows(True)
        self.velocity_plot_options_action.arrow_magnification.setCurrentIndex(0)

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
