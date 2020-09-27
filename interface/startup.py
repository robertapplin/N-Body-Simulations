# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5 import QtWidgets

from qt.ui.mainwindow_ui import Ui_MainWindow
from qt.presenter import NBodySimulationsPresenter
from qt.view import NBodySimulationsView

import sys


class MainGUI(QtWidgets.QMainWindow):
    """ Wrapper class for setting the main window"""
    def __init__(self, parent=None):
        super(MainGUI, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        view = NBodySimulationsView(self.ui)
        self.presenter = NBodySimulationsPresenter(view)


def qapp():
    if QtWidgets.QApplication.instance():
        return QtWidgets.QApplication.instance()
    return QtWidgets.QApplication(sys.argv)


if __name__ == "__main__":
    app = qapp()
    window = MainGUI()
    window.show()
    app.exec_()
