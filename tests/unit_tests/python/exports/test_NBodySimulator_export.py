# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from nbodysimulations import NBodySimulator


def test_that_creating_an_NBodySimulator_does_not_raise():
    _ = NBodySimulator("Simulator")


def test_that_getName_returns_the_correct_name():
    model = NBodySimulator("Simulator")
    assert model.getName() == "Simulator"
