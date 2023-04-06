# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.qt.table_item_delegates import ColourItemDelegate, DoubleItemDelegate, StringItemDelegate
from n_body_simulations.test_helpers.dummy_class_helper import DummyBodyTable
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

from PyQt5.QtWidgets import QTableWidget

enable_test_mode()


def test_that_creating_a_ColourItemDelegate_does_not_raise_an_exception():
    table = QTableWidget()
    _ = ColourItemDelegate(table)


def test_that_creating_a_DoubleItemDelegate_does_not_raise_an_exception():
    table = DummyBodyTable()
    _ = DoubleItemDelegate(table, DoubleItemDelegate.Mass)


def test_DoubleItemDelegate_handle_item_exited_sets_hovered_row_to_minus_one():
    table = DummyBodyTable()
    delegate = DoubleItemDelegate(table, DoubleItemDelegate.Mass)

    delegate.hovered_row = 0
    delegate.handle_item_exited(None)

    assert delegate.hovered_row == -1


def test_that_creating_a_StringItemDelegate_does_not_raise_an_exception():
    table = DummyBodyTable()
    _ = StringItemDelegate(table)
