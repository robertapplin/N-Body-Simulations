# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from nbodysimulations import NBodySimulator


def test_that_creating_a_simulator_does_not_raise():
    _ = NBodySimulator()


def test_that_getName_returns_the_correct_name():
    model = NBodySimulator()
    model.setName("Simulator")
    assert model.getName() == "Simulator"
