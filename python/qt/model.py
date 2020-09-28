# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import random


class NBodySimulationsModel:

    def __init__(self):
        self._initial_body_parameters = {"Sun": tuple([0, 0, 0, 0])}
        self._number_of_bodies = 1

    def initial_body_parameters(self) -> dict:
        return self._initial_body_parameters

    def number_of_bodies(self) -> int:
        return self._number_of_bodies

    def remove_body(self, body_name: str) -> None:
        del self._initial_body_parameters[body_name]
        self._number_of_bodies -= 1

    def add_body(self, body_name: str) -> None:
        self._initial_body_parameters[body_name] = tuple([random.uniform(-1, 1), random.uniform(-1, 1), 0, 0])
        self._number_of_bodies += 1

    def position(self, body_name: str) -> tuple:
        parameters = self._initial_body_parameters[body_name]
        return tuple([parameters[0], parameters[1]])
