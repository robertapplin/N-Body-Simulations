# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtCore import QCoreApplication


def enable_test_mode():
    # Required for:
    # - Silent error catching by preventing QMessageBox error messages.
    # - Allows the main interface to close after it opens.
    # - Makes sure resources are registered when testing.
    QCoreApplication.setApplicationName("test")
