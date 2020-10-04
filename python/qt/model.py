# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from nbodysimulations import NBodySimulator, Vector2D
from qt.error_catcher import catch_errors


class NBodySimulationsModel:

    def __init__(self):
        self._simulator = NBodySimulator()
        self.add_body("Sun", 1.0, 0.0, 0.0)

        self._simulation_results = None

    def initial_body_parameters(self) -> dict:
        initial_body_parameters = dict()

        for body_name in self._simulator.bodyNames():
            initial_body_parameters[body_name] = tuple([self.mass(body_name), self.initial_position(body_name),
                                                        self.initial_velocity(body_name)])
        return initial_body_parameters

    def number_of_bodies(self) -> int:
        return self._simulator.numberOfBodies()

    @catch_errors()
    def remove_body(self, body_name: str) -> None:
        self.reset_simulation()
        self._simulator.removeBody(body_name)

    @catch_errors()
    def add_body(self, body_name: str, mass: float, x: float, y: float) -> bool:
        self.reset_simulation()
        self._simulator.addBody(body_name, mass, Vector2D(x, y), Vector2D(0.0, 0.0))

        # If this point is reached, the body has been added successfully
        return True

    def set_time_step(self, time_step: float) -> None:
        self._simulator.setTimeStep(time_step)

    def time_step(self) -> float:
        return self._simulator.timeStep()

    def set_duration(self, duration: float) -> None:
        self._simulator.setDuration(duration)

    def duration(self) -> float:
        return self._simulator.duration()

    @catch_errors()
    def set_mass(self, body_name: str, mass: float) -> None:
        self._simulator.setMass(body_name, mass)

    @catch_errors()
    def mass(self, body_name: str) -> float:
        return self._simulator.mass(body_name)

    @catch_errors()
    def set_x_position(self, body_name: str, x: float) -> None:
        self._simulator.setXPosition(body_name, x)

    @catch_errors()
    def set_y_position(self, body_name: str, y: float) -> None:
        self._simulator.setYPosition(body_name, y)

    @catch_errors()
    def initial_position(self, body_name: str) -> Vector2D:
        return self._simulator.initialPosition(body_name)

    @catch_errors()
    def set_x_velocity(self, body_name: str, vx: float) -> None:
        self._simulator.setXVelocity(body_name, vx)

    @catch_errors()
    def set_y_velocity(self, body_name: str, vy: float) -> None:
        self._simulator.setYVelocity(body_name, vy)

    @catch_errors()
    def initial_velocity(self, body_name: str) -> Vector2D:
        return self._simulator.initialVelocity(body_name)

    def run_simulation(self):
        if self._simulator.hasDataChanged():
            success = self._simulator.runSimulation()
            self._simulation_results = self.simulation_results() if success else None
        return success

    def simulation_results(self):
        # Construct simulation results
        return dict()

    def start_simulation(self):
        pass

    def pause_simulation(self):
        pass
