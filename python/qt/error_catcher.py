# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtWidgets import QMessageBox

from functools import wraps


class ErrorReporter(QMessageBox):
    """A class for displaying an error message using a QMessageBox."""

    def __init__(self, message: str = ""):
        """Initialize the error reporter with an empty message."""
        super(ErrorReporter, self).__init__()

        self.setWindowTitle("Warning!")
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)

        self._error_message = message

    def __del__(self):
        """Display an error message, if present, upon deletion of the ErrorReporter object."""
        if self._error_message:
            self.setText(self._error_message)
            self.exec_()


def catch_errors(silent: bool = False):
    """A decorator function used to catch errors or exceptions in class member functions."""

    def decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except Exception as ex:
                if not silent:
                    ErrorReporter(str(ex))
        return wrapper
    return decorator
