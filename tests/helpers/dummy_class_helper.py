# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.body_marker import BodyMarker
from n_body_simulations.error_catcher import catch_errors
from n_body_simulations.simulation_animator import SimulationAnimator
from NBodySimulations import Vector2D

import matplotlib as mpl
mpl.use('agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class DummyBodyTable(QTableWidget):
    """A class used as a dummy body data table for the purposes of testing."""
    itemExited = pyqtSignal(QTableWidgetItem)

    def __init__(self):
        super(DummyBodyTable, self).__init__(None)


class DummyErrorProneClass:
    """A class used for testing the error catcher by causing various errors and exceptions."""

    def __init__(self):
        pass

    def cause_an_uncaught_exception(self):
        raise RuntimeError("This is a RuntimeError.")

    @catch_errors()
    def cause_an_exception(self):
        raise RuntimeError("This is a RuntimeError.")

    @catch_errors()
    def divide_by_zero(self):
        return 10 / 0

    @catch_errors()
    def index_out_of_range(self):
        test_list = [0, 1, 2, 3]
        return test_list[4]

    @catch_errors()
    def function_that_returns_nothing(self):
        _ = 1 + 2

    @catch_errors()
    def function_that_returns_a_value(self):
        return 1.0


class DummyInteractivePlot:
    """A class used as a dummy interactive plot for the purposes of testing the animator."""

    def __init__(self):
        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)

        self._ax = self._figure.add_subplot(111)
        self.animator = SimulationAnimator(self._figure)

        self.lines = {"Sun": self._ax.plot(0.0, 0.0)[0]}
        self.body_markers = {"Sun":
                             BodyMarker(self._canvas, "green", "Sun", 1.0, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))}
