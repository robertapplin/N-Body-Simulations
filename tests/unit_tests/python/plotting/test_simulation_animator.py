# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.test_helpers.dummy_class_helper import DummyInteractivePlot
from NBodySimulations import Vector2D


@pytest.fixture
def dummy_plot():
    plot = DummyInteractivePlot()
    positions = {"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0), 2.0: Vector2D(2.0, 2.0),
                         3.0: Vector2D(3.0, 3.0)}}
    velocities = {"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0), 2.0: Vector2D(2.0, 2.0),
                          3.0: Vector2D(3.0, 3.0)}}
    plot.animator.set_simulation_data(tuple([positions, velocities]))
    return plot


def test_that_enable_will_make_the_animator_active(dummy_plot):
    dummy_plot.animator.enable(dummy_plot.lines)
    assert dummy_plot.animator.is_enabled()


def test_that_disable_will_disable_the_animator(dummy_plot):
    dummy_plot.animator.enable(dummy_plot.lines)
    dummy_plot.animator.disable()

    assert not dummy_plot.animator.is_enabled()


def test_that_set_simulation_data_will_set_the_simulation_data_in_the_animator(dummy_plot):
    assert dummy_plot.animator.positional_data() == {"Sun": {0.0: Vector2D(0.0, 0.0), 1.0: Vector2D(1.0, 1.0),
                                                             2.0: Vector2D(2.0, 2.0), 3.0: Vector2D(3.0, 3.0)}}


def test_that_time_step_will_return_the_expected_time_step(dummy_plot):
    assert dummy_plot.animator.time_step() == 1.0


def test_that_duration_will_return_the_expected_simulation_duration(dummy_plot):
    assert dummy_plot.animator.duration() == 3.0
