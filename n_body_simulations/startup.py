# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import sys

from n_body_simulations.xml.interface_resources_rc import qInitResources, qCleanupResources
from n_body_simulations.qt.model import NBodySimulationsModel
from n_body_simulations.qt.presenter import NBodySimulationsPresenter
from n_body_simulations.qt.view import NBodySimulationsView

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication


def q_app():
    """Create or get a QApplication instance."""
    if QApplication.instance():
        return QApplication.instance()
    return QApplication(sys.argv)


def startup_widget():
    """Create and open the NBodySimulator widget in a window. Close it immediately if it is being tested."""
    app = q_app()
    qInitResources()

    view = NBodySimulationsView()
    model = NBodySimulationsModel()
    presenter = NBodySimulationsPresenter(view, model)

    presenter.open_widget()
    if QCoreApplication.applicationName() != "test":
        app.exec_()
    qCleanupResources()


if __name__ == "__main__":
    startup_widget()
