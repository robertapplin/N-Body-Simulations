from nbodysimulations import NBodySimulator

import pytest


def test_that_creating_an_NBodySimulator_does_not_raise():
    _ = NBodySimulator("Simulator")


def test_that_getName_returns_the_correct_name():
    model = NBodySimulator("Simulator")
    assert model.getName() == "Simulator"
