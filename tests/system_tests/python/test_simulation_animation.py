# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.test_helpers.dummy_class_helper import DummyInteractivePlot
from NBodySimulations import Vector2D


@pytest.fixture
def dummy_plot():
    plot = DummyInteractivePlot()
    masses = {"Sun": {0.0: 1.0, 1.0: 1.0, 2.0: 1.0, 3.0: 1.0}}
    positions = {"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0), 2.0: Vector2D(2.0, 2.0),
                         3.0: Vector2D(3.0, 3.0)}}
    velocities = {"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0), 2.0: Vector2D(2.0, 2.0),
                          3.0: Vector2D(3.0, 3.0)}}
    plot.animator.set_simulation_data(tuple([masses, positions, velocities]))
    return plot


def test_that_the_animator_will_start_pause_play_and_stop_without_error(dummy_plot):
    dummy_plot.animator.start(dummy_plot.lines)
    dummy_plot.animator.pause()
    dummy_plot.animator.play()
    dummy_plot.animator.stop()

    # Suppress a warning that an animation wasn't rendered
    dummy_plot.animator._animation._draw_was_started = True
