# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020


class NBodySimulationsModel:

    def __init__(self):
        self._initial_body_parameters = {"Sun": tuple([1.0, 0.0, 0.0, 0.0, 0.0])}
        self._number_of_bodies = 1

    def initial_body_parameters(self) -> dict:
        return self._initial_body_parameters

    def number_of_bodies(self) -> int:
        return self._number_of_bodies

    def remove_body(self, body_name: str) -> None:
        del self._initial_body_parameters[body_name]
        self._number_of_bodies -= 1

    def add_body(self, body_name: str, mass: float, x: float, y: float) -> None:
        self._initial_body_parameters[body_name] = tuple([mass, x, y, 0.0, 0.0])
        self._number_of_bodies += 1

    def parameters(self, body_name: str) -> tuple:
        if body_name in self._initial_body_parameters:
            return self._initial_body_parameters[body_name]
        return None
