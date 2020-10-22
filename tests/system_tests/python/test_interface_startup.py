# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.main_gui import start_gui

from PyQt5.QtCore import QCoreApplication


def test_that_the_interface_opens_without_an_error():
    # Required for the main interface to close after it opens
    QCoreApplication.setApplicationName("test")

    # Attempts to open the main interface
    start_gui()
