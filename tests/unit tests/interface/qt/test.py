# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from qt.model import NBodySimulationsModel

import pytest


def test_number_of_bodies_returns_expected_value():
    model = NBodySimulationsModel()
    assert model.number_of_bodies() == 1
