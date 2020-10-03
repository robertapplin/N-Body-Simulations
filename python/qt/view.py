# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtCore import pyqtSignal, QObject

from plotting.interactive_plot import InteractivePlot
from qt.add_body_dialog import AddBodyDialog
from qt.ui.main_window_ui import Ui_MainWindow


class NBodySimulationsView(Ui_MainWindow, QObject):
    selectedBodyChanged = pyqtSignal(str)
    removeBodySignal = pyqtSignal()
    addBodySignal = pyqtSignal()
    playPauseSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(NBodySimulationsView, self).__init__()
        self.setupUi(parent)

        self.interactive_plot = InteractivePlot()

        self.plotLayout.addWidget(self.interactive_plot.canvas())

        self.cbBodyNames.currentTextChanged.connect(lambda text: self.emit_selected_body_changed(text))
        self.pbRemoveBody.clicked.connect(self.emit_remove_body_clicked)
        self.pbAddBody.clicked.connect(self.emit_add_body_clicked)
        self.pbPlayPause.clicked.connect(self.emit_play_pause_clicked)

    def emit_selected_body_changed(self, text: str) -> None:
        self.selectedBodyChanged.emit(text)

    def emit_remove_body_clicked(self) -> None:
        self.removeBodySignal.emit()

    def emit_add_body_clicked(self) -> None:
        self.addBodySignal.emit()

    def emit_play_pause_clicked(self) -> None:
        self.playPauseSignal.emit()

    def clear(self) -> None:
        self.interactive_plot.clear()
        self.cbBodyNames.clear()

    def reset_view(self, bodies: dict) -> None:
        self.clear()
        self.add_bodies(bodies)

    def remove_body(self, body_name: str) -> None:
        self.cbBodyNames.removeItem(self.cbBodyNames.currentIndex())
        self.interactive_plot.remove_body(body_name)

    def add_bodies(self, body_parameters: dict) -> None:
        for body_name, parameters in body_parameters.items():
            self.cbBodyNames.addItem(body_name)
            self.interactive_plot.draw_body(body_name, parameters[1], parameters[2])

        self.cbBodyNames.setCurrentIndex(0)

    def add_body(self, body_name: str, parameters: tuple) -> None:
        self.cbBodyNames.addItem(body_name)
        self.cbBodyNames.setCurrentIndex(self.cbBodyNames.count() - 1)

        self.interactive_plot.draw_body(body_name, parameters[1], parameters[2])

    def set_mass(self, mass: float) -> None:
        self.dsbMass.setValue(mass)

    def set_position(self, x: float, y: float) -> None:
        self.dsbXPosition.setValue(x)
        self.dsbYPosition.setValue(y)

    def selected_body(self) -> str:
        return self.cbBodyNames.currentText()

    def set_as_simulating(self, simulating: bool) -> None:
        self.pbPlayPause.setText("Pause" if simulating else "Play")

    def is_simulating(self) -> bool:
        return self.pbPlayPause.text() != "Play"

    @staticmethod
    def open_add_body_dialog() -> tuple:
        dialog = AddBodyDialog()
        dialog.exec_()
        return dialog.new_body_data()
