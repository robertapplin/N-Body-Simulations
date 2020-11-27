# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.test_helpers.mock_class_helper import MockNBodySimulationsModel, MockNBodySimulationsPresenter
from n_body_simulations.view import NBodySimulationsView

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest


def setup_view():
    view = NBodySimulationsView()
    model = MockNBodySimulationsModel()
    presenter = MockNBodySimulationsPresenter(view, model)
    view.subscribe_presenter(presenter)
    return view, presenter


def test_that_remove_clicked_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    QTest.mouseClick(view.pbRemoveBody, Qt.LeftButton)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.RemoveBodyClicked)


def test_that_add_body_clicked_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    view.add_single_body_action.line_edit.setText("Earth")
    QTest.mouseClick(view.add_single_body_action.push_button, Qt.LeftButton)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.AddBodyClicked, "Earth")
    assert view.add_single_body_action.line_edit.text() == ""


def test_that_add_bodies_clicked_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    view.add_multiple_bodies_action.spin_box.setValue(5)
    QTest.mouseClick(view.add_multiple_bodies_action.push_button, Qt.LeftButton)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.AddBodiesClicked, 5)
    assert view.add_multiple_bodies_action.spin_box.value() == 1


def test_that_time_step_changed_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    view.time_step_action.double_spin_box.setValue(5.0)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.TimeStepChanged, 5.0)


def test_that_duration_changed_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    view.duration_action.double_spin_box.setValue(600.0)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.DurationChanged, 600.0)


def test_that_play_pause_clicked_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    QTest.mouseClick(view.pbPlayPause, Qt.LeftButton)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.PlayPauseClicked)
