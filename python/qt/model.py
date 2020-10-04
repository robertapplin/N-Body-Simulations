# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from nbodysimulations import NBodySimulator, Vector2D
from qt.error_catcher import catch_errors


class NBodySimulationsModel:

    def __init__(self):
        self._simulator = NBodySimulator()
        self._simulator.addBody("Sun", 1.0, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0))

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
        self._simulator.removeBody(body_name)

    def add_body(self, body_name: str, mass: float, x: float, y: float) -> None:
        self._simulator.addBody(body_name, mass, Vector2D(x, y), Vector2D(0.0, 0.0))

    @catch_errors()
    def mass(self, body_name: str) -> float:
        return self._simulator.mass(body_name)

    @catch_errors()
    def initial_position(self, body_name: str) -> Vector2D:
        return self._simulator.initialPosition(body_name)

    @catch_errors()
    def initial_velocity(self, body_name: str) -> Vector2D:
        return self._simulator.initialVelocity(body_name)
