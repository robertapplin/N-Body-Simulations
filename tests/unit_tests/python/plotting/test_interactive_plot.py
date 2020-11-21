# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.interactive_plot import InteractivePlot
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode
from NBodySimulations import Vector2D

enable_test_mode()


@pytest.fixture
def interactive_plot():
    return InteractivePlot()


def test_that_add_body_will_add_a_body_to_the_plot(interactive_plot):
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")

    assert list(interactive_plot._initial_data.keys()) == ["Earth"]
    assert list(interactive_plot._body_markers.keys()) == ["Earth"]


def test_that_remove_body_will_remove_a_body_from_the_plot(interactive_plot):
    interactive_plot.add_body("Sun", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "red")
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")

    assert list(interactive_plot._initial_data.keys()) == ["Sun", "Earth"]
    assert list(interactive_plot._body_markers.keys()) == ["Sun", "Earth"]

    interactive_plot.remove_body("Sun")

    assert list(interactive_plot._initial_data.keys()) == ["Earth"]
    assert list(interactive_plot._body_markers.keys()) == ["Earth"]


def test_that_get_body_colour_returns_the_expected_colour_for_a_body(interactive_plot):
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")
    assert interactive_plot.get_body_colour("Earth") == "green"


def test_that_update_body_colour_will_update_the_colour_of_a_body(interactive_plot):
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")
    interactive_plot.update_body_colour("Earth", "red")

    assert interactive_plot.get_body_colour("Earth") == "red"


def test_that_update_body_name_will_update_the_name_of_a_body(interactive_plot):
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")
    interactive_plot.update_body_name("Earth", "Sun")

    assert list(interactive_plot._initial_data.keys()) == ["Sun"]
    assert list(interactive_plot._body_markers.keys()) == ["Sun"]


def test_that_update_body_position_will_update_the_position_of_a_body(interactive_plot):
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")
    interactive_plot.update_body_position("Earth", Vector2D(1.0, 1.0))

    assert interactive_plot._body_markers["Earth"]._position == Vector2D(1.0, 1.0)


def test_that_update_body_velocity_will_update_the_velocity_of_a_body(interactive_plot):
    interactive_plot.add_body("Earth", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "green")
    interactive_plot.update_body_velocity("Earth", Vector2D(1.0, 1.0))

    assert interactive_plot._body_markers["Earth"]._velocity == Vector2D(1.0, 1.0)


def test_that_update_axes_limits_will_update_the_axes_limits_for_a_single_body(interactive_plot):
    interactive_plot.add_body("Sun", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "red")

    interactive_plot.update_axes_limits()

    assert interactive_plot.get_axes_limits() == tuple([-0.5, 0.5, -0.5, 0.5])


def test_that_update_axes_limits_will_update_the_axes_limits_to_the_expected_values(interactive_plot):
    interactive_plot.add_body("Sun", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "red")
    interactive_plot.add_body("Earth", Vector2D(1.0, 1.0), Vector2D(0.0, 0.0), "green")

    interactive_plot.update_axes_limits()

    assert interactive_plot.get_axes_limits() == tuple([0.0, 1.0, 0.0, 1.0])


def test_that_update_axes_limits_will_update_the_axes_limits_for_a_non_square_layout(interactive_plot):
    interactive_plot.add_body("Sun", Vector2D(0.0, 0.0), Vector2D(0.0, 0.0), "red")
    interactive_plot.add_body("Earth", Vector2D(0.1, 0.5), Vector2D(0.0, 0.0), "green")

    interactive_plot.update_axes_limits()

    assert interactive_plot.get_axes_limits() == tuple([-0.2, 0.3, 0.0, 0.5])
