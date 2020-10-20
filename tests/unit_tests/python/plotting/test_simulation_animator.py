# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest
import sys
from directory_helper import PYTHON_DIRECTORY

from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Required to find python modules in parent directories
sys.path.append(PYTHON_DIRECTORY)

from plotting.simulation_animator import SimulationAnimator


class DummyInteractivePlot:
    """A class used as a dummy interactive plot for the purposes of testing the animator."""

    def __init__(self):
        """Initialize the dummy interactive plot."""
        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)

        self._ax = self._figure.add_subplot(111)
        self.animator = SimulationAnimator(self._figure)

        self.lines = {"Sun": self._ax.plot(0.0, 0.0)[0]}


@pytest.fixture
def dummy_plot():
    plot = DummyInteractivePlot()
    plot.animator.set_simulation_data({"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0),
                                               2.0: Vector2D(2.0, 2.0), 3.0: Vector2D(3.0, 3.0)}})
    return plot


def test_that_enable_will_make_the_animator_active(dummy_plot):
    dummy_plot.animator.enable(dummy_plot.lines)
    assert dummy_plot.animator.is_enabled()


def test_that_disable_will_disable_the_animator(dummy_plot):
    dummy_plot.animator.enable(dummy_plot.lines)
    dummy_plot.animator.disable()

    assert not dummy_plot.animator.is_enabled()


def test_that_set_simulation_data_will_set_the_simulation_data_in_the_animator(dummy_plot):
    assert dummy_plot.animator.simulation_data() == {"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0),
                                                             2.0: Vector2D(2.0, 2.0), 3.0: Vector2D(3.0, 3.0)}}


def test_that_time_step_will_return_the_expected_time_step(dummy_plot):
    assert dummy_plot.animator.time_step() == 1.0


def test_that_duration_will_return_the_expected_simulation_duration(dummy_plot):
    assert dummy_plot.animator.duration() == 3.0
