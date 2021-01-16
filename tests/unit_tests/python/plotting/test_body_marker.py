# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.test_helpers.dummy_class_helper import DummyInteractivePlot

from PyQt5.QtCore import Qt


import sys
from PyQt5.QtWidgets import QApplication


@pytest.fixture
def app():
    """Create or get a QApplication instance."""
    if QApplication.instance():
        return QApplication.instance()
    return QApplication(sys.argv)


@pytest.fixture
def dummy_plot():
    plot = DummyInteractivePlot()
    return plot


def test_that_get_colour_will_get_the_colour_of_the_body_marker(app, dummy_plot):
    assert dummy_plot.body_markers["Sun"].get_colour() == "green"
    app.exit()


def test_that_set_colour_will_set_the_colour_of_the_body_marker(app, dummy_plot):
    dummy_plot.body_markers["Sun"].set_colour("red")
    assert dummy_plot.body_markers["Sun"].get_colour() == "red"
    app.exit()


def test_that_set_mass_will_set_the_mass_of_the_body(app, dummy_plot):
    dummy_plot.body_markers["Sun"].set_mass(5.0)
    assert dummy_plot.body_markers["Sun"]._mass == 5.0
    app.exit()


def test_that_set_position_will_set_the_position_of_the_body(app, dummy_plot):
    dummy_plot.body_markers["Sun"].set_position(1.0, 1.0)
    assert dummy_plot.body_markers["Sun"].mouse_drag_start(1.0, 1.0)
    app.exit()


def test_that_mouse_drag_start_will_return_true_when_the_mouse_position_is_above_the_marker(app, dummy_plot):
    assert dummy_plot.body_markers["Sun"].mouse_drag_start(0.0, 0.0)
    assert dummy_plot.body_markers["Sun"].get_override_cursor() == Qt.ClosedHandCursor
    app.exit()


def test_that_mouse_drag_start_will_return_false_when_the_mouse_position_is_not_above_the_marker(app, dummy_plot):
    assert not dummy_plot.body_markers["Sun"].mouse_drag_start(1.0, 1.0)
    app.exit()


def test_that_mouse_drag_stop_will_return_true_if_the_marker_is_currently_being_dragged(app, dummy_plot):
    assert dummy_plot.body_markers["Sun"].mouse_drag_start(0.0, 0.0)
    assert dummy_plot.body_markers["Sun"].mouse_drag_stop(0.1, 0.1)
    assert dummy_plot.body_markers["Sun"].get_override_cursor() == Qt.OpenHandCursor
    app.exit()


def test_that_mouse_drag_stop_will_return_false_if_the_marker_is_not_being_dragged(app, dummy_plot):
    assert not dummy_plot.body_markers["Sun"].mouse_drag_stop(0.0, 0.0)
    app.exit()


def test_that_mouse_moved_will_return_true_if_the_marker_is_currently_being_dragged(app, dummy_plot):
    assert dummy_plot.body_markers["Sun"].mouse_drag_start(0.0, 0.0)
    assert dummy_plot.body_markers["Sun"].mouse_moved(0.1, 0.1)
    assert dummy_plot.body_markers["Sun"].get_override_cursor() == Qt.ClosedHandCursor
    app.exit()


def test_that_mouse_moved_will_return_false_if_the_marker_is_not_being_dragged(app, dummy_plot):
    assert not dummy_plot.body_markers["Sun"].mouse_moved(0.0, 0.0)
    app.exit()


def test_that_remove_body_will_not_raise(app, dummy_plot):
    dummy_plot.body_markers["Sun"].remove_body()
    app.exit()


def test_that_create_body_will_not_raise(app, dummy_plot):
    dummy_plot.body_markers["Sun"].create_body()
    app.exit()


def test_that_refresh_will_not_raise(app, dummy_plot):
    dummy_plot.body_markers["Sun"].refresh()
    app.exit()
