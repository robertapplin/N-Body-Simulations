# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest
import sys

from PyQt5.QtCore import QCoreApplication
from directory_helper import PYTHON_DIRECTORY

# Required to find python modules in parent directories
sys.path.append(PYTHON_DIRECTORY)

from qt.model import NBodySimulationsModel

# Required to allow silent error catching
QCoreApplication.setApplicationName("test")


@pytest.fixture
def model():
    simulator_model = NBodySimulationsModel()
    simulator_model.add_body("Earth", 0.5, 1.0, 1.0)
    return simulator_model


def test_that_initializing_NBodySimulationsModel_does_not_raise():
    _ = NBodySimulationsModel()


def test_that_number_of_bodies_returns_the_expected_value(model):
    assert model.number_of_bodies() == 2


def test_that_mass_returns_the_expected_value(model):
    assert model.mass("Earth") == 0.5


def test_that_mass_fails_silently_if_an_invalid_body_name_is_provided(model):
    _ = model.mass("Not a body")


def test_that_initial_position_returns_the_expected_value(model):
    position = model.initial_position("Earth")

    assert position.x == 1.0
    assert position.y == 1.0


def test_that_initial_position_fails_silently_if_an_invalid_body_name_is_provided(model):
    _ = model.initial_position("Not a body")


def test_that_initial_velocity_returns_the_expected_value(model):
    position = model.initial_velocity("Earth")

    assert position.x == 0.0
    assert position.y == 0.0


def test_that_initial_velocity_fails_silently_if_an_invalid_body_name_is_provided(model):
    _ = model.initial_velocity("Not a body")


def test_that_add_body_will_add_a_body_as_expected(model):
    model.add_body("Mars", 0.2, 3.0, 4.0)

    mass = model.mass("Mars")
    position = model.initial_position("Mars")
    velocity = model.initial_velocity("Mars")

    assert mass == 0.2
    assert position.x == 3.0
    assert position.y == 4.0
    assert velocity.x == 0.0
    assert velocity.y == 0.0


def test_that_adding_a_body_which_already_exists_fails_silently(model):
    model.add_body("Earth", 0.5, 3.0, 4.0)
    assert model.number_of_bodies() == 2


def test_that_remove_body_will_remove_a_body_as_expected(model):
    model.add_body("Mars", 0.2, 3.0, 4.0)
    model.remove_body("Mars")

    assert model.number_of_bodies() == 2


def test_that_remove_body_fails_silently_if_an_invalid_body_name_is_provided(model):
    model.remove_body("Not a body")


def test_that_time_step_returns_the_expected_value(model):
    assert model.time_step() == 1.0


def test_that_set_time_step_will_set_the_time_step(model):
    model.set_time_step(2.0)
    assert model.time_step() == 2.0


def test_that_duration_returns_the_expected_value(model):
    assert model.duration() == 500.0


def test_that_set_duration_will_set_the_duration(model):
    model.set_duration(600.0)
    assert model.duration() == 600.0


def test_that_initial_body_parameters_will_return_the_expected_parameters(model):
    model.add_body("Mars", 0.2, 3.0, 4.0)
    body_parameters = model.initial_body_parameters()

    assert "Earth" in body_parameters
    assert "Mars" in body_parameters

    earth_parameters = body_parameters["Earth"]
    assert earth_parameters[0] == 0.5
    assert earth_parameters[1].x == 1.0
    assert earth_parameters[1].y == 1.0

    mars_parameters = body_parameters["Mars"]
    assert mars_parameters[0] == 0.2
    assert mars_parameters[1].x == 3.0
    assert mars_parameters[1].y == 4.0


def test_that_set_x_position_will_set_the_x_position_of_a_body_as_expected(model):
    model.set_x_position("Earth", 5.0)

    position = model.initial_position("Earth")
    assert position.x == 5.0


def test_that_set_y_position_will_set_the_y_position_of_a_body_as_expected(model):
    model.set_y_position("Earth", 5.0)

    position = model.initial_position("Earth")
    assert position.y == 5.0


def test_that_set_x_velocity_will_set_the_x_velocity_of_a_body_as_expected(model):
    model.set_x_velocity("Earth", 5.0)

    velocity = model.initial_velocity("Earth")
    assert velocity.x == 5.0


def test_that_set_y_velocity_will_set_the_y_velocity_of_a_body_as_expected(model):
    model.set_y_velocity("Earth", 5.0)

    velocity = model.initial_velocity("Earth")
    assert velocity.y == 5.0


def test_that_set_x_position_fails_silently_if_an_invalid_body_name_is_provided(model):
    model.set_x_position("Not a body", 5.0)


def test_that_set_y_position_fails_silently_if_an_invalid_body_name_is_provided(model):
    model.set_y_position("Not a body", 5.0)


def test_that_set_x_velocity_fails_silently_if_an_invalid_body_name_is_provided(model):
    model.set_x_velocity("Not a body", 5.0)


def test_that_set_y_velocity_fails_silently_if_an_invalid_body_name_is_provided(model):
    model.set_y_velocity("Not a body", 5.0)
