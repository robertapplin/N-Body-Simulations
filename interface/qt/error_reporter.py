# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5 import QtWidgets


class ErrorReporter(QtWidgets.QMessageBox):

    def __init__(self):
        super(ErrorReporter, self).__init__()

        self.setWindowTitle("Warning!")
        self.setIcon(QtWidgets.QMessageBox.Warning)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self._error_message = ""

    def __del__(self):
        if self._error_message:
            self.setText(self._error_message)
            self.exec_()

    def report_error(self, message: str) -> None:
        self._error_message = message
