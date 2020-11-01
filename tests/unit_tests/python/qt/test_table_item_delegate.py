# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.table_item_delegate import TableItemDelegate

from PyQt5.QtWidgets import QTableWidget


def test_that_creating_a_TableItemDelegate_does_not_raise_an_exception():
    table = QTableWidget()
    _ = TableItemDelegate(table, TableItemDelegate.Mass)


def test_that_the_TableItemDelegate_has_a_spinbox_with_the_correct_parameters():
    table = QTableWidget()
    item_delegate = TableItemDelegate(table, TableItemDelegate.Mass)

    assert item_delegate.box.minimum() == 0.000001
    assert item_delegate.box.maximum() == 100.0
    assert item_delegate.box.singleStep() == 0.1
