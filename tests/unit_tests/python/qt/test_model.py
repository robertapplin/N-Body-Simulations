# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import sys
from directory_helper import PYTHON_DIRECTORY

# Required to find python modules in parent directories
sys.path.append(PYTHON_DIRECTORY)

from qt.model import NBodySimulationsModel


def test_number_of_bodies_returns_expected_value():
    model = NBodySimulationsModel()
    assert model.number_of_bodies() == 1
