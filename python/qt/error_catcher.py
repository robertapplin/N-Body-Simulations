# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5 import QtWidgets

from functools import wraps


class ErrorReporter(QtWidgets.QMessageBox):

    def __init__(self, message=""):
        super(ErrorReporter, self).__init__()

        self.setWindowTitle("Warning!")
        self.setIcon(QtWidgets.QMessageBox.Warning)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self._error_message = message

    def __del__(self):
        if self._error_message:
            self.setText(self._error_message)
            self.exec_()


def catch_errors(silent=False):
    def decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            try:
                function(self, *args, **kwargs)
            except Exception as ex:
                if not silent:
                    ErrorReporter(str(ex))
        return wrapper
    return decorator
