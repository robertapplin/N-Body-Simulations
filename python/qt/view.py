# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtCore import pyqtSignal, QObject, QSignalBlocker

from plotting.interactive_plot import InteractivePlot
from qt.add_body_dialog import AddBodyDialog
from qt.ui.main_window_ui import Ui_MainWindow

from nbodysimulations import Vector2D


class NBodySimulationsView(Ui_MainWindow, QObject):
    selectedBodyChangedSignal = pyqtSignal(str)
    removeBodySignal = pyqtSignal()
    addBodySignal = pyqtSignal()
    timeStepChangedSignal = pyqtSignal(float)
    durationChangedSignal = pyqtSignal(float)
    playPauseSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(NBodySimulationsView, self).__init__()
        self.setupUi(parent)

        self.interactive_plot = InteractivePlot()

        self.plotLayout.addWidget(self.interactive_plot.canvas())

        self.cbBodyNames.currentTextChanged.connect(lambda text: self.emit_selected_body_changed(text))
        self.pbRemoveBody.clicked.connect(self.emit_remove_body_clicked)
        self.pbAddBody.clicked.connect(self.emit_add_body_clicked)
        self.dsbTimeStep.valueChanged.connect(lambda value: self.emit_time_step_changed(value))
        self.dsbDuration.valueChanged.connect(lambda value: self.emit_duration_changed(value))
        self.pbPlayPause.clicked.connect(self.emit_play_pause_clicked)

    def emit_selected_body_changed(self, text: str) -> None:
        self.selectedBodyChangedSignal.emit(text)

    def emit_remove_body_clicked(self) -> None:
        self.removeBodySignal.emit()

    def emit_add_body_clicked(self) -> None:
        self.addBodySignal.emit()

    def emit_time_step_changed(self, value: float) -> None:
        self.timeStepChangedSignal.emit(value)

    def emit_duration_changed(self, value: float) -> None:
        self.durationChangedSignal.emit(value)

    def emit_play_pause_clicked(self) -> None:
        self.playPauseSignal.emit()

    def clear(self) -> None:
        self.interactive_plot.clear()
        self.cbBodyNames.clear()

    def reset_view(self, bodies: dict, time_step: float, duration: float) -> None:
        self.clear()
        self.add_bodies(bodies)
        self.set_time_step(time_step)
        self.set_duration(duration)

    def remove_body(self, body_name: str) -> None:
        self.cbBodyNames.removeItem(self.cbBodyNames.currentIndex())
        self.interactive_plot.remove_body(body_name)

    def add_bodies(self, body_parameters: dict) -> None:
        for body_name, parameters in body_parameters.items():
            self.cbBodyNames.addItem(body_name)
            self.interactive_plot.draw_body(body_name, parameters[1].x, parameters[1].y)

        self.cbBodyNames.setCurrentIndex(0)

    def add_body(self, body_name: str, position: Vector2D) -> None:
        self.cbBodyNames.addItem(body_name)
        self.cbBodyNames.setCurrentIndex(self.cbBodyNames.count() - 1)

        self.interactive_plot.draw_body(body_name, position.x, position.y)

    def set_time_step(self, time_step: float) -> None:
        QSignalBlocker(self.dsbTimeStep)
        self.dsbTimeStep.setValue(time_step)

    def set_duration(self, duration: float) -> None:
        QSignalBlocker(self.dsbDuration)
        self.dsbDuration.setValue(duration)

    def set_mass(self, mass: float) -> None:
        QSignalBlocker(self.dsbMass)
        self.dsbMass.setValue(mass)

    def set_position(self, position: Vector2D) -> None:
        self.dsbXPosition.setValue(position.x)
        self.dsbYPosition.setValue(position.y)

    def selected_body(self) -> str:
        return self.cbBodyNames.currentText()

    def set_as_simulating(self, simulating: bool) -> None:
        self.pbPlayPause.setText("Pause" if simulating else "Play")

    def is_simulating(self) -> bool:
        return self.pbPlayPause.text() != "Play"

    def enable_play_pause(self, enable: bool) -> None:
        self.pbPlayPause.setEnabled(enable)

    @staticmethod
    def open_add_body_dialog() -> tuple:
        dialog = AddBodyDialog()
        dialog.exec_()
        return dialog.new_body_data()
