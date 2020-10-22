# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.simulation_animator import SimulationAnimator
from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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


def test_that_the_animator_will_start_pause_play_and_stop_without_error(dummy_plot):
    dummy_plot.animator.start(dummy_plot.lines)
    dummy_plot.animator.pause()
    dummy_plot.animator.play()
    dummy_plot.animator.stop()
