# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from NBodySimulations import Vector2D

from PyQt5.QtCore import pyqtSignal, QObject


class MockNBodySimulationsModel:
    """A mock class used for mocking the model."""

    def __init__(self):
        pass

    @staticmethod
    def initial_body_parameters() -> dict:
        return dict()

    def remove_body(self, body_name: str) -> None:
        pass

    @staticmethod
    def add_body(body_name: str, mass: float, x: float, y: float, vx: float = 0.0, vy: float = 0.0) -> bool:
        return True

    @staticmethod
    def body_names():
        return ["Earth"]

    def set_time_step(self, time_step: float) -> None:
        pass

    @staticmethod
    def time_step() -> float:
        return 1.0

    def set_duration(self, duration: float) -> None:
        pass

    @staticmethod
    def duration() -> float:
        return 500.0

    @staticmethod
    def number_of_bodies() -> int:
        return 3

    def set_name(self, old_name: str, new_name: str) -> None:
        pass

    def set_mass(self, body_name: str, mass: float) -> None:
        pass

    def set_x_position(self, body_name: str, x: float) -> None:
        pass

    def set_y_position(self, body_name: str, x: float) -> None:
        pass

    @staticmethod
    def initial_position(body_name: str) -> Vector2D:
        return Vector2D(0.0, 0.0)

    @staticmethod
    def initial_velocity(body_name: str) -> Vector2D:
        return Vector2D(0.0, 0.0)

    def set_x_velocity(self, body_name: str, vx: float) -> None:
        pass

    def set_y_velocity(self, body_name: str, vy: float) -> None:
        pass

    @staticmethod
    def initial_data(body_name: str) -> tuple:
        return tuple([1.0, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0)])

    @staticmethod
    def run_simulation() -> bool:
        return True

    @staticmethod
    def has_data_changed() -> bool:
        return True

    @staticmethod
    def simulation_results() -> dict:
        return dict()


class MockNBodySimulationsView(QObject):
    """A mock class used for mocking the view."""
    removeBodyClickedSignal = pyqtSignal()
    addBodyClickedSignal = pyqtSignal(str)
    addBodiesClickedSignal = pyqtSignal(int)
    bodyNameChangedSignal = pyqtSignal(str, str)
    massChangedSignal = pyqtSignal(str, float)
    xPositionChangedSignal = pyqtSignal(str, float)
    yPositionChangedSignal = pyqtSignal(str, float)
    xVelocityChangedSignal = pyqtSignal(str, float)
    yVelocityChangedSignal = pyqtSignal(str, float)
    timeStepChangedSignal = pyqtSignal(float)
    durationChangedSignal = pyqtSignal(float)
    playPauseClickedSignal = pyqtSignal()

    bodyMovedSignal = pyqtSignal(str, float, float)
    bodyVelocityChangedSignal = pyqtSignal(str, float, float)

    def __init__(self):
        super(MockNBodySimulationsView, self).__init__()

    def reset_view(self, bodies: dict, time_step: float, duration: float):
        pass

    def remove_body(self, body_name: str) -> None:
        pass

    def add_body(self, body_name: str, initial_data: tuple) -> None:
        pass

    def update_body_name(self, old_name: str, new_name: str) -> None:
        pass

    def update_body_position(self, body_name: str, position: Vector2D) -> None:
        pass

    def update_body_velocity(self, body_name: str, velocity: Vector2D) -> None:
        pass

    def set_name(self, body_name: str) -> None:
        pass

    def set_as_playing(self, playing: bool) -> None:
        pass

    @staticmethod
    def is_simulating() -> bool:
        return False

    def enable_view(self, enable: bool) -> None:
        pass

    @staticmethod
    def selected_bodies():
        return ["Earth"]

    @staticmethod
    def open_add_body_dialog():
        return "Earth", 1.0, 0.0, 0.0

    def start_simulation(self, simulation_results: dict) -> None:
        pass

    def stop_simulation(self) -> None:
        pass

    def pause_simulation(self) -> None:
        pass

    def play_simulation(self) -> None:
        pass

    @staticmethod
    def get_axes_limits() -> tuple:
        return 0.0, 1.0, 0.0, 1.0
