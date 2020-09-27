# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5 import QtCore

from plotting.interactive_plot import InteractivePlot
from qt.add_body_dialog import AddBodyDialog


class NBodySimulationsView(QtCore.QObject):
    removeBodySignal = QtCore.pyqtSignal()
    addBodySignal = QtCore.pyqtSignal()
    playPauseSignal = QtCore.pyqtSignal()

    def __init__(self, ui_form):
        super(NBodySimulationsView, self).__init__()

        self.ui = ui_form

        self.interactive_plot = InteractivePlot()

        self.ui.plotLayout.addWidget(self.interactive_plot.canvas())

        self.ui.pbRemoveBody.clicked.connect(self.emit_remove_body_clicked)
        self.ui.pbAddBody.clicked.connect(self.emit_add_body_clicked)
        self.ui.pbPlayPause.clicked.connect(self.emit_play_pause_clicked)

    def emit_remove_body_clicked(self) -> None:
        self.removeBodySignal.emit()

    def emit_add_body_clicked(self) -> None:
        self.addBodySignal.emit()

    def emit_play_pause_clicked(self) -> None:
        self.playPauseSignal.emit()

    def clear(self) -> None:
        self.interactive_plot.clear()
        self.ui.cbBodyNames.clear()

    def reset_view(self, bodies: dict) -> None:
        self.clear()
        self.add_bodies(bodies)

    def remove_body(self, body_name: str) -> None:
        self.ui.cbBodyNames.removeItem(self.ui.cbBodyNames.currentIndex())
        self.interactive_plot.remove_body(body_name)

    def add_bodies(self, body_parameters: dict) -> None:
        for body_name, parameters in body_parameters.items():
            self.ui.cbBodyNames.addItem(body_name)
            self.interactive_plot.draw_body(body_name, parameters[0], parameters[1])

        self.ui.cbBodyNames.setCurrentIndex(0)

    def add_body(self, body_name: str, position: tuple) -> None:
        self.ui.cbBodyNames.addItem(body_name)
        self.ui.cbBodyNames.setCurrentIndex(self.ui.cbBodyNames.count() - 1)

        self.interactive_plot.draw_body(body_name, position[0], position[1])

    def selected_body(self) -> str:
        return self.ui.cbBodyNames.currentText()

    def set_as_simulating(self, simulating: bool) -> None:
        self.ui.pbPlayPause.setText("Pause" if simulating else "Play")

    def is_simulating(self) -> bool:
        return self.ui.pbPlayPause.text() != "Play"

    @staticmethod
    def open_add_body_dialog() -> str:
        dialog = AddBodyDialog()
        dialog.exec_()
        return dialog.new_body_name()
