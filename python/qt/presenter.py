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
        self.view.timeStepChangedSignal.connect(lambda time_step: self.handle_time_step_changed(time_step))
        self.view.durationChangedSignal.connect(lambda duration: self.handle_duration_changed(duration))
        self.view.playPauseSignal.connect(self.handle_play_pause_clicked)

        self.view.reset_view(self.model.initial_body_parameters(), self.model.time_step(), self.model.duration())

    def handle_selected_body_changed(self, body_name: str) -> None:
        if body_name:
            self.view.set_mass(self.model.mass(body_name))
            self.view.set_position(self.model.initial_position(body_name))

    def handle_remove_body_clicked(self) -> None:
        if self.model.number_of_bodies() > 1:
            body_name = self.view.selected_body()
            self.model.remove_body(body_name)
            self.view.remove_body(body_name)

    def handle_add_body_clicked(self) -> None:
        if self.model.number_of_bodies() < 5:
            self._add_new_body()

    def handle_time_step_changed(self, time_step) -> None:
        self.model.set_time_step(time_step)

    def handle_duration_changed(self, duration) -> None:
        self.model.set_duration(duration)

    def handle_play_pause_clicked(self) -> None:
        play_clicked = not self.view.is_simulating()
        self.view.set_as_simulating(play_clicked)

        first_run = True
        if play_clicked and first_run:
            self.view.enable_play_pause(False)
            self.model.run_simulation()
            self.view.enable_play_pause(True)
            self.model.start_simulation()
        elif play_clicked:
            self.model.start_simulation()
        else:
            self.model.pause_simulation()

    def _add_new_body(self) -> None:
        body_name, mass, x, y = self.view.open_add_body_dialog()
        if body_name is not None:
            self.model.add_body(body_name, mass, x, y)
            self.view.add_body(body_name, self.model.initial_position(body_name))
