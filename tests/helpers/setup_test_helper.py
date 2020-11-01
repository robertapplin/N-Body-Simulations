# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.interface_resources_rc import qInitResources, qCleanupResources

from PyQt5.QtCore import QCoreApplication


def enable_test_mode():
    # Required for silent error catching by preventing QMessageBox error messages.
    # Also required for the main interface to close after it opens.
    QCoreApplication.setApplicationName("test")


def register_resource_files():
    # Required for registering resource files so that they can be found.
    qInitResources()


def cleanup_resource_files():
    # Required for cleaning up resource files.
    qCleanupResources()
