# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtCore import QCoreApplication


def enable_test_mode():
    # Required for silent error catching by preventing QMessageBox error messages.
    # Also required for the main interface to close after it opens.
    QCoreApplication.setApplicationName("test")
