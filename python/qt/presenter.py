# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.error_catcher import catch_errors
from n_body_simulations.model import NBodySimulationsModel


class NBodySimulationsPresenter:

    def __init__(self, view):
        self.view = view
        self.model = NBodySimulationsModel()

        # Temporarily here for development
        self.model.add_body("Sun", 1.0, 0.0, 0.0)
        self.model.add_body("Earth", 0.000003, 1.0, 0.0, 0.0, 0.015)

        self.view.removeBodyClickedSignal.connect(self.handle_remove_body_clicked)
        self.view.addBodyClickedSignal.connect(self.handle_add_body_clicked)
        self.view.bodyNameChangedSignal.connect(lambda old_name, new_name: self.handle_body_name_changed(old_name,
                                                                                                         new_name))
        self.view.massChangedSignal.connect(lambda body_name, mass: self.handle_mass_changed(body_name, mass))
        self.view.xPositionChangedSignal.connect(lambda body_name, x: self.handle_x_position_changed(body_name, x))
        self.view.yPositionChangedSignal.connect(lambda body_name, y: self.handle_y_position_changed(body_name, y))
        self.view.xVelocityChangedSignal.connect(lambda body_name, vx: self.handle_x_velocity_changed(body_name, vx))
        self.view.yVelocityChangedSignal.connect(lambda body_name, vy: self.handle_y_velocity_changed(body_name, vy))
        self.view.timeStepChangedSignal.connect(lambda time_step: self.handle_time_step_changed(time_step))
        self.view.durationChangedSignal.connect(lambda duration: self.handle_duration_changed(duration))
        self.view.playPauseClickedSignal.connect(self.handle_play_pause_clicked)

        self.view.reset_view(self.model.initial_body_parameters(), self.model.time_step(), self.model.duration())

    def handle_remove_body_clicked(self) -> None:
        body_name = self.view.selected_body()
        if body_name and self.model.number_of_bodies() > 1:
            self.model.remove_body(body_name)
            self.view.remove_body(body_name)

    def handle_add_body_clicked(self) -> None:
        if self.model.number_of_bodies() < 5:
            self._add_new_body()

    @catch_errors()
    def handle_body_name_changed(self, old_name: str, new_name: str) -> None:
        if new_name not in self.model.body_names():
            self.model.set_name(old_name, new_name)
            self.view.update_body_name(old_name, new_name)
        else:
            self.view.set_name(old_name)
            raise ValueError(f"Could not change body name: The body '{new_name}' already exists.")

    def handle_mass_changed(self, body_name: str, mass: float) -> None:
        self.model.set_mass(body_name, mass)

    def handle_x_position_changed(self, body_name: str, x: float) -> None:
        self.model.set_x_position(body_name, x)
        self.view.update_body_position(body_name, self.model.initial_position(body_name))

    def handle_y_position_changed(self, body_name: str, y: float) -> None:
        self.model.set_y_position(body_name, y)
        self.view.update_body_position(body_name, self.model.initial_position(body_name))

    def handle_x_velocity_changed(self, body_name: str, vx: float) -> None:
        self.model.set_x_velocity(body_name, vx)

    def handle_y_velocity_changed(self, body_name: str, vy: float) -> None:
        self.model.set_y_velocity(body_name, vy)

    def handle_time_step_changed(self, time_step: float) -> None:
        self.model.set_time_step(time_step)

    def handle_duration_changed(self, duration: float) -> None:
        self.model.set_duration(duration)

    def handle_play_pause_clicked(self) -> None:
        play_clicked = not self.view.is_simulating()
        self.view.set_as_playing(play_clicked)

        data_changed = self.model.has_data_changed()

        if play_clicked and data_changed:
            self.view.stop_simulation()
            self._run_simulation()

        if play_clicked:
            self.view.play_simulation()
        else:
            self.view.pause_simulation()

    def _add_new_body(self) -> None:
        body_name, mass, x, y = self.view.open_add_body_dialog()
        if body_name is not None:
            success = self.model.add_body(body_name, mass, x, y)
            if success:
                self.view.add_body(body_name, self.model.initial_data(body_name))

    def _run_simulation(self) -> None:
        self.view.enable_view(False)
        success = self.model.run_simulation()
        self.view.enable_view(True)
        if success:
            self.view.start_simulation(self.model.simulation_results())
        else:
            self.view.set_as_playing(False)
