# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import unit_test_setup
from model import NBodySimulationsModel


def test_number_of_bodies_returns_expected_value():
    model = NBodySimulationsModel()
    assert model.number_of_bodies() == 1
