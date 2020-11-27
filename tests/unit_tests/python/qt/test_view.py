# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
#from n_body_simulations.interface_resources_rc import qInitResources, qCleanupResources
#from n_body_simulations.startup import q_app
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


def test_that_remove_button_click_notifies_the_presenter(mocker):
    view, presenter = setup_view()
    presenter_notify_presenter = mocker.spy(presenter, 'notify_presenter')

    QTest.mouseClick(view.pbRemoveBody, Qt.LeftButton)

    presenter_notify_presenter.assert_called_once_with(view.ViewEvent.RemoveBodyClicked)
