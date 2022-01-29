# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.qt.custom_actions import DoubleSpinBoxAction, LineEditButtonAction, SpinBoxButtonAction
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

from PyQt5.QtWidgets import QToolButton

enable_test_mode()


def test_that_creating_a_DoubleSpinBoxAction_does_not_raise_an_exception(qtbot):
    _ = DoubleSpinBoxAction("Duration: ", DoubleSpinBoxAction.TimeStep)


def test_that_adding_a_DoubleSpinBoxAction_to_a_tool_button_does_not_raise_an_exception(qtbot):
    double_spinbox_action = DoubleSpinBoxAction("Duration: ", DoubleSpinBoxAction.Duration)

    tool_button = QToolButton()
    tool_button.addAction(double_spinbox_action)


def test_that_a_DoubleSpinBoxAction_with_the_correct_spin_box_parameters_is_created(qtbot):
    double_spinbox_action = DoubleSpinBoxAction("Duration: ", DoubleSpinBoxAction.Duration)

    assert double_spinbox_action.double_spin_box.value() == 500.0
    assert double_spinbox_action.double_spin_box.minimum() == 0.0
    assert double_spinbox_action.double_spin_box.maximum() == 10000.0
    assert double_spinbox_action.double_spin_box.singleStep() == 10.0
    assert double_spinbox_action.double_spin_box.suffix() == " d"


def test_that_creating_a_LineEditButtonAction_does_not_raise_an_exception(qtbot):
    _ = LineEditButtonAction("Add Body", "[a-zA-Z][a-zA-Z0-9]*(?:[-])[a-zA-Z0-9]*")


def test_that_adding_a_LineEditButtonAction_to_a_tool_button_does_not_raise_an_exception(qtbot):
    line_edit_spinbox_action = LineEditButtonAction("Add Body", "[a-zA-Z][a-zA-Z0-9]*(?:[-])[a-zA-Z0-9]*")

    tool_button = QToolButton()
    tool_button.addAction(line_edit_spinbox_action)


def test_that_creating_a_SpinBoxButtonAction_does_not_raise_an_exception(qtbot):
    _ = SpinBoxButtonAction("Add Bodies")


def test_that_adding_a_SpinBoxButtonAction_to_a_tool_button_does_not_raise_an_exception(qtbot):
    spinbox_buttton_action = SpinBoxButtonAction("Add Bodies")

    tool_button = QToolButton()
    tool_button.addAction(spinbox_buttton_action)
