# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.qt.body_data_table import BodyDataTableWidget, ColourTableWidget
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

enable_test_mode()


def test_that_creating_a_BodyDataTableWidget_does_not_raise_an_exception(qtbot):
    _ = BodyDataTableWidget()


def test_that_creating_a_ColourTableWidget_does_not_raise_an_exception(qtbot):
    _ = ColourTableWidget()
