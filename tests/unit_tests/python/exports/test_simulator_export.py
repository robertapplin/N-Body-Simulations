# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from NBodySimulations import NBodySimulator, Vector2D


@pytest.fixture
def simulator():
    sim = NBodySimulator()
    sim.addBody("Sun", 1.0, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))
    return sim


def test_that_creating_a_simulator_does_not_raise():
    _ = NBodySimulator()


def test_that_addBody_is_exposed_to_python(simulator):
    simulator.addBody("Earth", 0.5, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))


def test_that_removeBody_is_exposed_to_python(simulator):
    simulator.addBody("Earth", 0.5, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))
    simulator.removeBody("Earth")


def test_that_timeStep_is_exposed_to_python(simulator):
    assert simulator.timeStep() == 0.0


def test_that_setTimeStep_is_exposed_to_python(simulator):
    simulator.setTimeStep(2.0)
    assert simulator.timeStep() == 2.0


def test_that_duration_is_exposed_to_python(simulator):
    assert simulator.duration() == 0.0


def test_that_setDuration_is_exposed_to_python(simulator):
    simulator.setDuration(600.0)
    assert simulator.duration() == 600.0


def test_that_numberOfBodies_is_exposed_to_python(simulator):
    assert simulator.numberOfBodies() == 1


def test_that_bodyNames_is_exposed_to_python(simulator):
    assert simulator.bodyNames() == ["Sun"]


def test_that_addBody_will_add_a_body(simulator):
    simulator.addBody("Earth", 0.5, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))
    assert simulator.bodyNames() == ["Sun", "Earth"]


def test_that_removeBody_will_remove_a_body(simulator):
    simulator.addBody("Earth", 0.5, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))
    simulator.removeBody("Sun")

    assert simulator.bodyNames() == ["Earth"]


def test_that_setName_is_exposed_to_python(simulator):
    simulator.setName("Sun", "Earth")
    assert simulator.bodyNames() == ["Earth"]


def test_that_initialMass_is_exposed_to_python(simulator):
    assert simulator.initialMass("Sun") == 1.0


def test_that_setMass_is_exposed_to_python(simulator):
    simulator.setMass("Sun", 5.0)
    assert simulator.initialMass("Sun") == 5.0


def test_that_initialPosition_is_exposed_to_python(simulator):
    position = simulator.initialPosition("Sun")

    assert position.x == 0.0
    assert position.y == 0.0


def test_that_setXPosition_is_exposed_to_python(simulator):
    simulator.setXPosition("Sun", 1.0)
    position = simulator.initialPosition("Sun")

    assert position.x == 1.0


def test_that_setYPosition_is_exposed_to_python(simulator):
    simulator.setYPosition("Sun", 1.0)
    position = simulator.initialPosition("Sun")

    assert position.y == 1.0


def test_that_initialVelocity_is_exposed_to_python(simulator):
    velocity = simulator.initialVelocity("Sun")

    assert velocity.x == 0.0
    assert velocity.y == 0.0


def test_that_setXVelocity_is_exposed_to_python(simulator):
    simulator.setXVelocity("Sun", 1.0)
    velocity = simulator.initialVelocity("Sun")

    assert velocity.x == 1.0


def test_that_setYVelocity_is_exposed_to_python(simulator):
    simulator.setYVelocity("Sun", 1.0)
    velocity = simulator.initialVelocity("Sun")

    assert velocity.y == 1.0


def test_that_hasDataChanged_is_exposed_to_python(simulator):
    assert simulator.hasDataChanged()


def test_that_runSimulation_is_exposed_to_python(simulator):
    simulator.setTimeStep(1.0)
    simulator.setDuration(500.0)
    simulator.runSimulation()

    assert not simulator.hasDataChanged()


def test_that_simulationResults_is_exposed_to_python(simulator):
    simulator.setTimeStep(1.0)
    simulator.setDuration(500.0)
    simulator.runSimulation()

    times, data = simulator.simulationResults("Sun").items()

    assert data[0][0.0] == 1.0
    assert data[0][1.0] == 1.0
    assert data[0][2.0] == 1.0
    assert data[1][0.0] == Vector2D(0.0, 0.0)
    assert data[1][1.0] == Vector2D(0.0, 0.0)
    assert data[1][2.0] == Vector2D(0.0, 0.0)
    assert data[2][0.0] == Vector2D(0.0, 0.0)
    assert data[2][1.0] == Vector2D(0.0, 0.0)
    assert data[2][2.0] == Vector2D(0.0, 0.0)
