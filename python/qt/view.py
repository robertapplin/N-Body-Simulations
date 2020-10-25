# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.add_body_dialog import AddBodyDialog
from n_body_simulations.interactive_plot import InteractivePlot
from n_body_simulations.main_window_ui import Ui_MainWindow
from n_body_simulations.signal_blocker import SignalBlocker
from NBodySimulations import Vector2D

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QDoubleSpinBox, QStyledItemDelegate, QTableWidgetItem


TABLE_NAME_INDEX = 0
TABLE_MASS_INDEX = 1
TABLE_X_INDEX = 2
TABLE_Y_INDEX = 3
TABLE_VX_INDEX = 4
TABLE_VY_INDEX = 5


class ItemDelegate(QStyledItemDelegate):

    def __init__(self, parent, min_value=None, max_value=None, step=None):
        super(ItemDelegate, self).__init__(parent)

        self._min = min_value
        self._max = max_value
        self._step = step
        self._decimals = 6

    def createEditor(self, parent, style, index) -> None:
        box = QDoubleSpinBox(parent)
        box.setDecimals(self._decimals)

        if self._step is not None:
            box.setSingleStep(self._step)
        if self._min is not None:
            box.setMinimum(self._min)
        if self._max is not None:
            box.setMaximum(self._max)

        return box


class NBodySimulationsView(Ui_MainWindow, QObject):
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

    def __init__(self, parent=None):
        super(NBodySimulationsView, self).__init__()
        self.setupUi(parent)

        self.setup_table_widget()

        self.interactive_plot = InteractivePlot()
        self.plotLayout.addWidget(self.interactive_plot.canvas())

        self.pbRemoveBody.clicked.connect(self.emit_remove_body_clicked)
        self.pbAddBody.clicked.connect(self.emit_add_body_clicked)
        self.pbEdit.clicked.connect(self.handle_edit_clicked)
        self.pbStop.clicked.connect(self.handle_stop_clicked)
        self.pbPlayPause.clicked.connect(self.emit_play_pause_clicked)
        self.twBodyData.cellClicked.connect(lambda row, column: self.handle_cell_clicked(row, column))
        self.twBodyData.cellChanged.connect(lambda row, column: self.handle_body_data_changed(row, column))
        self.dsbTimeStep.valueChanged.connect(lambda value: self.emit_time_step_changed(value))
        self.dsbDuration.valueChanged.connect(lambda value: self.emit_duration_changed(value))

        self._selected_body = None

    def setup_table_widget(self) -> None:
        mass_item_delegate = ItemDelegate(self.twBodyData, min_value=0.000001, step=0.1)
        other_item_delegate = ItemDelegate(self.twBodyData, min_value=-1000.0, max_value=1000.0, step=0.1)

        self.twBodyData.setItemDelegateForColumn(TABLE_MASS_INDEX, mass_item_delegate)
        self.twBodyData.setItemDelegateForColumn(TABLE_X_INDEX, other_item_delegate)
        self.twBodyData.setItemDelegateForColumn(TABLE_Y_INDEX, other_item_delegate)
        self.twBodyData.setItemDelegateForColumn(TABLE_VX_INDEX, other_item_delegate)
        self.twBodyData.setItemDelegateForColumn(TABLE_VY_INDEX, other_item_delegate)

    def emit_remove_body_clicked(self) -> None:
        self.removeBodyClickedSignal.emit()

    def emit_add_body_clicked(self) -> None:
        self.addBodyClickedSignal.emit()

    def emit_play_pause_clicked(self) -> None:
        self.playPauseClickedSignal.emit()

    def emit_time_step_changed(self, value: float) -> None:
        self.timeStepChangedSignal.emit(value)

    def emit_duration_changed(self, value: float) -> None:
        self.durationChangedSignal.emit(value)

    def handle_cell_clicked(self, row_index: int, column_index: int) -> None:
        self._selected_body = self._body_at_index(row_index)

    def handle_body_data_changed(self, row_index: int, column_index: int) -> None:
        self.set_as_editing(True)

        signal_switcher = {TABLE_MASS_INDEX: self.massChangedSignal,
                           TABLE_X_INDEX: self.xPositionChangedSignal,
                           TABLE_Y_INDEX: self.yPositionChangedSignal,
                           TABLE_VX_INDEX: self.xVelocityChangedSignal,
                           TABLE_VY_INDEX: self.yVelocityChangedSignal}

        signal = signal_switcher.get(column_index, None)
        if signal is not None:
            signal.emit(self._selected_body, self._get_table_value(row_index, column_index))
        else:
            self.bodyNameChangedSignal.emit(self._selected_body, self._body_at_index(row_index))

    def handle_edit_clicked(self) -> None:
        self.set_as_playing(False)
        self.interactive_plot.disable_animation()

    def handle_stop_clicked(self) -> None:
        self.set_as_playing(False)
        self.interactive_plot.stop_animation()

    def clear(self) -> None:
        self.interactive_plot.clear()
        self.twBodyData.clearContents()

    def reset_view(self, bodies: dict, time_step: float, duration: float) -> None:
        self.clear()
        self.add_bodies(bodies)
        self.set_time_step(time_step)
        self.set_duration(duration)

    def selected_body(self) -> str:
        selected_index = self._selected_row_index()
        if selected_index != -1:
            return self._body_at_index(selected_index)
        return None

    def remove_body(self, body_name: str) -> None:
        self.set_as_editing(True)

        self.twBodyData.removeRow(self._selected_row_index())

        self.interactive_plot.remove_body(body_name)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.show_legend()
        self.interactive_plot.draw()

    def add_bodies(self, body_parameters: dict) -> None:
        self.set_as_editing(True)

        for body_name, parameters in body_parameters.items():
            self.add_body_to_table(body_name, parameters)
            self.interactive_plot.add_body(body_name, parameters[1])

        self.interactive_plot.show_legend()
        self.interactive_plot.draw()

    def add_body(self, body_name: str, initial_data: tuple) -> None:
        self.set_as_editing(True)

        self.add_body_to_table(body_name, initial_data)

        self.interactive_plot.add_body(body_name, initial_data[1])
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.show_legend()
        self.interactive_plot.draw()

    def add_body_to_table(self, body_name: str, body_data: tuple) -> None:
        _ = SignalBlocker(self.twBodyData)
        row_index = self.twBodyData.rowCount()

        self.twBodyData.insertRow(row_index)
        self.twBodyData.setItem(row_index, TABLE_NAME_INDEX, QTableWidgetItem(body_name))
        self.twBodyData.setItem(row_index, TABLE_MASS_INDEX, self._create_table_value(body_data[0]))
        self.twBodyData.setItem(row_index, TABLE_X_INDEX, self._create_table_value(body_data[1].x))
        self.twBodyData.setItem(row_index, TABLE_Y_INDEX, self._create_table_value(body_data[1].y))
        self.twBodyData.setItem(row_index, TABLE_VX_INDEX, self._create_table_value(body_data[2].x))
        self.twBodyData.setItem(row_index, TABLE_VY_INDEX, self._create_table_value(body_data[2].y))

    def update_body_name(self, old_name: str, new_name: str) -> None:
        self.interactive_plot.update_body_name(old_name, new_name)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.show_legend()
        self.interactive_plot.draw()

    def update_body_position(self, body_name: str, position: Vector2D) -> None:
        self.interactive_plot.remove_body(body_name)
        self.interactive_plot.add_body(body_name, position)
        self.interactive_plot.update_axes_limits(initial_data=True)
        self.interactive_plot.draw()

    def set_name(self, body_name: str) -> None:
        _ = SignalBlocker(self.twBodyData)
        self.twBodyData.setItem(self._selected_row_index(), TABLE_NAME_INDEX, QTableWidgetItem(body_name))

    def set_time_step(self, time_step: float) -> None:
        _ = SignalBlocker(self.dsbTimeStep)
        self.dsbTimeStep.setValue(time_step)

    def set_duration(self, duration: float) -> None:
        _ = SignalBlocker(self.dsbDuration)
        self.dsbDuration.setValue(duration)

    def set_as_editing(self, editing: bool) -> None:
        self.pbEdit.setChecked(editing)
        if editing:
            self.handle_edit_clicked()

    def set_as_playing(self, playing: bool) -> None:
        self.pbPlayPause.setText("Pause" if playing else "Play")
        if playing:
            self.set_as_editing(False)

    def is_simulating(self) -> bool:
        return self.pbPlayPause.text() != "Play"

    def enable_view(self, enable: bool) -> None:
        self.twBodyData.setEnabled(enable)
        self.pbRemoveBody.setEnabled(enable)
        self.pbAddBody.setEnabled(enable)
        self.dsbTimeStep.setEnabled(enable)
        self.dsbDuration.setEnabled(enable)
        self.pbEdit.setEnabled(enable)
        self.pbStop.setEnabled(enable)
        self.pbPlayPause.setEnabled(enable)

    @staticmethod
    def open_add_body_dialog() -> tuple:
        dialog = AddBodyDialog()
        dialog.exec_()
        return dialog.new_body_data()

    def start_simulation(self, simulation_results: dict) -> None:
        self.interactive_plot.set_simulation_data(simulation_results)
        self.interactive_plot.update_axes_limits(initial_data=False)
        self.interactive_plot.start_animation()

    def stop_simulation(self) -> None:
        self.interactive_plot.stop_animation()

    def pause_simulation(self) -> None:
        self.interactive_plot.pause_animation()

    def play_simulation(self) -> None:
        self.interactive_plot.play_animation()

    @staticmethod
    def _create_table_value(value: float) -> QTableWidgetItem:
        item = QTableWidgetItem()
        item.setData(Qt.EditRole, value)
        return item

    def _get_table_value(self, row_index: int, column_index: int) -> float:
        return float(self.twBodyData.item(row_index, column_index).text())

    def _body_at_index(self, row_index: int) -> str:
        return self.twBodyData.item(row_index, 0).text()

    def _selected_row_index(self) -> int:
        selection_model = self.twBodyData.selectionModel()
        if selection_model.hasSelection():
            return selection_model.currentIndex().row()
        return -1
