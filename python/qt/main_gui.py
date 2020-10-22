# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import sys

from n_body_simulations.presenter import NBodySimulationsPresenter
from n_body_simulations.view import NBodySimulationsView

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainGUI(QMainWindow):
    """Wrapper class for setting the main window."""

    def __init__(self, parent=None):
        """Initialize the main window with a presenter (MVP)."""
        super(MainGUI, self).__init__(parent)

        view = NBodySimulationsView(self)
        self.presenter = NBodySimulationsPresenter(view)


def qapp():
    """Create or get a QApplication instance."""
    if QApplication.instance():
        return QApplication.instance()
    return QApplication(sys.argv)


def start_gui():
    """Startup the main GUI, but close it immediately if it is being tested."""
    app = qapp()
    window = MainGUI()
    window.show()
    if QCoreApplication.applicationName() != "test":
        app.exec_()
