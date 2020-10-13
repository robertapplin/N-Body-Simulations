# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from NBodySimulations import NBodySimulator, Vector2D
from qt.error_catcher import catch_errors


class NBodySimulationsModel:
    """A class used as a model for the main GUI (MVP)."""

    def __init__(self):
        """Initialize the model with an empty NBodySimulator."""
        self._simulator = NBodySimulator()

    def initial_body_parameters(self) -> dict:
        """Return the initial body parameters (mass, position and velocity) of all bodies."""
        initial_body_parameters = dict()

        for body_name in self._simulator.bodyNames():
            initial_body_parameters[body_name] = tuple([self.mass(body_name), self.initial_position(body_name),
                                                        self.initial_velocity(body_name)])
        return initial_body_parameters

    @catch_errors()
    def remove_body(self, body_name: str) -> None:
        """Removes the body with the specified name from the simulator."""
        self._simulator.removeBody(body_name)

    @catch_errors()
    def add_body(self, body_name: str, mass: float, x: float, y: float, vx: float = 0.0, vy: float = 0.0) -> bool:
        """Add a body to the simulator."""
        self._simulator.addBody(body_name, mass, Vector2D(x, y), Vector2D(vx, vy))

        # If this point is reached, the body has been added successfully
        return True

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
    def set_mass(self, body_name: str, mass: float) -> None:
        """Set the mass of the specified body in the simulator."""
        self._simulator.setMass(body_name, mass)

    @catch_errors()
    def mass(self, body_name: str) -> float:
        """Return the mass of the specified body stored by the simulator."""
        return self._simulator.mass(body_name)

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
    def run_simulation(self) -> bool:
        """Run the simulation if the data has changed since the last simulation."""
        if self.has_data_changed():
            self._simulator.runSimulation()

        # If this point is reached, the simulation has been successfully
        return True

    def has_data_changed(self):
        return self._simulator.hasDataChanged()

    @catch_errors()
    def simulation_results(self) -> dict:
        """Collect the simulation results from the simulator."""
        results = dict()
        for body_name in self._simulator.bodyNames():
            results[body_name] = self._simulator.simulatedPositions(body_name)
        return results
