# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.double_spinbox_action import DoubleSpinBoxAction

from PyQt5.QtWidgets import QToolButton


@pytest.fixture
def dummy_action():
    return DoubleSpinBoxAction("Duration: ", DoubleSpinBoxAction.Duration)


def test_that_creating_a_DoubleSpinBoxAction_does_not_raise_an_exception():
    _ = DoubleSpinBoxAction("Duration: ", DoubleSpinBoxAction.TimeStep)


def test_that_adding_a_DoubleSpinBoxAction_to_a_tool_button_does_not_raise_an_exception(dummy_action):
    tool_button = QToolButton()
    tool_button.addAction(dummy_action)


def test_that_a_DoubleSpinBoxAction_with_the_correct_spin_box_parameters_is_created(dummy_action):
    assert dummy_action.double_spin_box.value() == 500.0
    assert dummy_action.double_spin_box.minimum() == 0.0
    assert dummy_action.double_spin_box.maximum() == 10000.0
    assert dummy_action.double_spin_box.singleStep() == 10.0
    assert dummy_action.double_spin_box.suffix() == " d"
