# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.table_item_delegate import TableItemDelegate
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

from PyQt5.QtWidgets import QTableWidget

enable_test_mode()


def test_that_creating_a_TableItemDelegate_does_not_raise_an_exception():
    table = QTableWidget()
    _ = TableItemDelegate(table, TableItemDelegate.Mass)


def test_that_the_TableItemDelegate_has_a_spinbox_with_the_correct_parameters():
    table = QTableWidget()
    item_delegate = TableItemDelegate(table, TableItemDelegate.Mass)
    table.setItemDelegateForColumn(0, item_delegate)

    assert item_delegate.min == 0.000001
    assert item_delegate.max == 100.0
    assert item_delegate.step == 0.1
    assert item_delegate.decimals == 6
