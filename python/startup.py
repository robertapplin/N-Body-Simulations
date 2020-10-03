# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import sys

from PyQt5 import QtWidgets

from qt.presenter import NBodySimulationsPresenter
from qt.view import NBodySimulationsView


class MainGUI(QtWidgets.QMainWindow):
    """Wrapper class for setting the main window."""

    def __init__(self, parent=None):
        """Initialize the main window with a presenter (MVP)."""
        super(MainGUI, self).__init__(parent)

        view = NBodySimulationsView(self)
        self.presenter = NBodySimulationsPresenter(view)


def qapp():
    """Create or get a QApplication instance."""
    if QtWidgets.QApplication.instance():
        return QtWidgets.QApplication.instance()
    return QtWidgets.QApplication(sys.argv)


if __name__ == "__main__":
    app = qapp()
    window = MainGUI()
    window.show()
    app.exec_()
