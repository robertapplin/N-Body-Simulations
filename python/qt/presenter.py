# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from qt.model import NBodySimulationsModel


class NBodySimulationsPresenter:

    def __init__(self, view):
        self.view = view
        self.model = NBodySimulationsModel()

        self.view.selectedBodyChangedSignal.connect(lambda body_name: self.handle_selected_body_changed(body_name))
        self.view.removeBodySignal.connect(self.handle_remove_body_clicked)
        self.view.addBodySignal.connect(self.handle_add_body_clicked)
        self.view.massChangedSignal.connect(lambda body_name, mass: self.handle_mass_changed(body_name, mass))
        self.view.xPositionChangedSignal.connect(lambda body_name, x: self.handle_x_position_changed(body_name, x))
        self.view.yPositionChangedSignal.connect(lambda body_name, y: self.handle_y_position_changed(body_name, y))
        self.view.xVelocityChangedSignal.connect(lambda body_name, vx: self.handle_x_velocity_changed(body_name, vx))
        self.view.yVelocityChangedSignal.connect(lambda body_name, vy: self.handle_y_velocity_changed(body_name, vy))
        self.view.timeStepChangedSignal.connect(lambda time_step: self.handle_time_step_changed(time_step))
        self.view.durationChangedSignal.connect(lambda duration: self.handle_duration_changed(duration))
        self.view.playPauseSignal.connect(self.handle_play_pause_clicked)

        self.view.reset_view(self.model.initial_body_parameters(), self.model.time_step(), self.model.duration())

    def handle_selected_body_changed(self, body_name: str) -> None:
        if body_name:
            self.view.set_mass(self.model.mass(body_name))
            self.view.set_position(self.model.initial_position(body_name))
            self.view.set_velocity(self.model.initial_velocity(body_name))

    def handle_remove_body_clicked(self) -> None:
        if self.model.number_of_bodies() > 1:
            body_name = self.view.selected_body()
            self.model.remove_body(body_name)
            self.view.remove_body(body_name)

    def handle_add_body_clicked(self) -> None:
        if self.model.number_of_bodies() < 5:
            self._add_new_body()

    def handle_mass_changed(self, body_name: str, mass: float) -> None:
        self.model.set_mass(body_name, mass)

    def handle_x_position_changed(self, body_name: str, x: float) -> None:
        self.model.set_x_position(body_name, x)

    def handle_y_position_changed(self, body_name: str, y: float) -> None:
        self.model.set_y_position(body_name, y)

    def handle_x_velocity_changed(self, body_name: str, vx: float) -> None:
        self.model.set_x_velocity(body_name, vx)

    def handle_y_velocity_changed(self, body_name: str, vy: float) -> None:
        self.model.set_y_velocity(body_name, vy)

    def handle_time_step_changed(self, time_step) -> None:
        self.model.set_time_step(time_step)

    def handle_duration_changed(self, duration) -> None:
        self.model.set_duration(duration)

    def handle_play_pause_clicked(self) -> None:
        play_clicked = not self.view.is_simulating()
        self.view.set_as_simulating(play_clicked)

        if play_clicked:
            self.view.enable_play_pause(False)
            success = self.model.run_simulation()
            self.view.enable_play_pause(True)
            if success:
                self.model.start_simulation()
        else:
            self.model.pause_simulation()

    def _add_new_body(self) -> None:
        body_name, mass, x, y = self.view.open_add_body_dialog()
        if body_name is not None:
            success = self.model.add_body(body_name, mass, x, y)
            if success:
                self.view.add_body(body_name, self.model.initial_position(body_name))
