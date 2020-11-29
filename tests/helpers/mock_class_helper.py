# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from enum import Enum

from NBodySimulations import Vector2D

from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QWidget


class MockNBodySimulationsModel(QThread):
    """A mock class used for mocking the model."""
    simulationFinished = pyqtSignal()
    simulationError = pyqtSignal(str)

    def __init__(self):
        super(MockNBodySimulationsModel, self).__init__(None)

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
    def initial_position(_: str) -> Vector2D:
        return Vector2D(0.0, 0.0)

    @staticmethod
    def initial_velocity(_: str) -> Vector2D:
        return Vector2D(0.0, 0.0)

    def set_x_velocity(self, body_name: str, vx: float) -> None:
        pass

    def set_y_velocity(self, body_name: str, vy: float) -> None:
        pass

    @staticmethod
    def initial_data(_: str) -> tuple:
        return tuple([1.0, Vector2D(0.0, 0.0), Vector2D(0.0, 0.0)])

    @staticmethod
    def run() -> None:
        pass

    @staticmethod
    def has_data_changed() -> bool:
        return True

    @staticmethod
    def simulation_results() -> dict:
        return dict()


class MockNBodySimulationsView(QWidget):
    """A mock class used for mocking the view."""
    class ViewEvent(Enum):
        RemoveBodyClicked = 1
        AddBodyClicked = 2
        AddBodiesClicked = 3
        TimeStepChanged = 4
        DurationChanged = 5
        NameChanged = 6
        MassChanged = 7
        XPositionChanged = 8
        YPositionChanged = 9
        VxPositionChanged = 10
        VyPositionChanged = 11
        PlayPauseClicked = 12
        BodyMovedOnPlot = 13
        BodyVelocityChangedOnPlot = 14

    def __init__(self):
        super(MockNBodySimulationsView, self).__init__()

    def subscribe_presenter(self, _):
        pass

    def reset_view(self, bodies: dict, time_step: float, duration: float):
        pass

    def remove_body(self, body_name: str) -> None:
        pass

    def add_body(self, body_name: str, initial_data: tuple) -> None:
        pass

    def update_body_name(self, old_name: str, new_name: str) -> None:
        pass

    def update_body_mass(self, body_name: str, mass: float) -> None:
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


class MockNBodySimulationsPresenter:
    """A mock class used for mocking the presenter."""

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def notify_presenter(self, event, *args) -> None:
        pass
