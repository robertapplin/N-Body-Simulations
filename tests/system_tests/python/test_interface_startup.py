# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest
import sys
from directory_helper import PYTHON_DIRECTORY

from PyQt5.QtCore import QCoreApplication

# Required to find python modules in parent directories
sys.path.append(PYTHON_DIRECTORY)

from qt.main_gui import start_gui


def test_that_the_interface_opens_without_an_error():
    # Required for the main interface to close after it opens
    QCoreApplication.setApplicationName("test")

    # Attempts to open the main interface
    start_gui()
