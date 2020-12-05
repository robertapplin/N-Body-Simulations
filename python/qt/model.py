# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.error_catcher import catch_errors
from n_body_simulations.xml_reader import get_user_interface_property
from NBodySimulations import NBodySimulator, Vector2D

from PyQt5.QtCore import pyqtSignal, QThread


class NBodySimulationsModel(QThread):
    """A class used as a model for the main GUI (MVP)."""
    simulationFinished = pyqtSignal()
    simulationError = pyqtSignal(str)

    time_dp = int(get_user_interface_property("time-dp"))

    def __init__(self):
        """Initialize the model with an empty NBodySimulator."""
        super(NBodySimulationsModel, self).__init__(None)
        self._simulator = NBodySimulator()

    def clear(self) -> None:
        """Clear all the data from the simulator."""
        self._simulator.clear()

    def initial_body_parameters(self) -> dict:
        """Return the initial body parameters (mass, position and velocity) of all bodies."""
        initial_body_parameters = dict()

        for body_name in self.body_names():
            initial_body_parameters[body_name] = self.initial_data(body_name)
        return initial_body_parameters

    @catch_errors()
    def remove_body(self, body_name: str) -> None:
        """Removes the body with the specified name from the simulator."""
        self._simulator.removeBody(body_name)

    @catch_errors()
    def add_body(self, body_name: str, mass: float, x: float, y: float, vx: float, vy: float) -> bool:
        """Add a body to the simulator."""
        self._simulator.addBody(body_name, mass, Vector2D(x, y), Vector2D(vx, vy))

        # If this point is reached, the body has been added successfully
        return True

    def body_names(self) -> list:
        """Returns the body names stored by the simulator."""
        return self._simulator.bodyNames()

    def set_time_step(self, time_step: float) -> None:
        """Set the time step used by the simulator."""
        self._simulator.setTimeStep(time_step)

    def time_step(self) -> float:
        """Return the time step stored by the simulator."""
        return self._simulator.timeStep()

    def set_duration(self, duration: float) -> None:
        """Set the simulation duration used by the simulator."""
        self._simulator.setDuration(duration)

    def duration(self) -> float:
        """Return the simulation duration stored by the simulator."""
        return self._simulator.duration()

    def number_of_bodies(self) -> int:
        """Return the number of bodies in the simulation setup."""
        return self._simulator.numberOfBodies()

    @catch_errors()
    def set_name(self, old_name: str, new_name: str) -> None:
        """Set a new name for the specified body in the simulator."""
        self._simulator.setName(old_name, new_name)

    @catch_errors()
    def set_mass(self, body_name: str, mass: float) -> None:
        """Set the mass of the specified body in the simulator."""
        self._simulator.setMass(body_name, mass)

    @catch_errors()
    def initial_mass(self, body_name: str) -> float:
        """Return the initial mass of the specified body stored by the simulator."""
        return self._simulator.initialMass(body_name)

    @catch_errors()
    def set_x_position(self, body_name: str, x: float) -> None:
        """Set the x position of the specified body in the simulator."""
        self._simulator.setXPosition(body_name, x)

    @catch_errors()
    def set_y_position(self, body_name: str, y: float) -> None:
        """Set the y position of the specified body in the simulator."""
        self._simulator.setYPosition(body_name, y)

    @catch_errors()
    def initial_position(self, body_name: str) -> Vector2D:
        """Return the initial position of the specified body stored by the simulator."""
        return self._simulator.initialPosition(body_name)

    @catch_errors()
    def set_x_velocity(self, body_name: str, vx: float) -> None:
        """Set the x velocity of the specified body in the simulator."""
        self._simulator.setXVelocity(body_name, vx)

    @catch_errors()
    def set_y_velocity(self, body_name: str, vy: float) -> None:
        """Set the y velocity of the specified body in the simulator."""
        self._simulator.setYVelocity(body_name, vy)

    @catch_errors()
    def initial_velocity(self, body_name: str) -> Vector2D:
        """Return the initial velocity of the specified body stored by the simulator."""
        return self._simulator.initialVelocity(body_name)

    @catch_errors()
    def initial_data(self, body_name: str) -> tuple:
        """Returns the initial data of the specified body stored by the simulator."""
        return tuple([self.initial_mass(body_name), self.initial_position(body_name), self.initial_velocity(body_name)])

    def has_data_changed(self) -> bool:
        """Returns true if the data held by the simulator has changed since the last simulation."""
        return self._simulator.hasDataChanged()

    def run(self) -> None:
        """Run the simulation if the data has changed since the last simulation."""
        try:
            self._simulator.runSimulation()
            self.simulationFinished.emit()
        except Exception as ex:
            self.simulationError.emit(str(ex))

    @catch_errors()
    def simulation_results(self) -> dict:
        """Collect the simulation results from the simulator."""
        position_data, velocity_data = dict(), dict()
        for body_name in self._simulator.bodyNames():
            position_data[body_name] = self._round_time_decimal_places(self._simulator.simulatedPositions(body_name))
            velocity_data[body_name] = self._round_time_decimal_places(self._simulator.simulatedVelocities(body_name))
        return position_data, velocity_data

    def _round_time_decimal_places(self, simulated_data: dict) -> dict:
        """
        This is necessary to prevent a bug caused by the infinite-length representation of some decimal numbers. For
        instance, 0.2 is represented as 0.200000000000001 and this can cause certain 'time' dict keys to not be found.
        """
        rounded_data = dict()
        for time, position in simulated_data.items():
            rounded_data[round(time, self.time_dp)] = position
        return rounded_data
