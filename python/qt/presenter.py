# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from qt.model import NBodySimulationsModel


class NBodySimulationsPresenter:

    def __init__(self, view):
        self.view = view
        self.model = NBodySimulationsModel()

        self.view.selectedBodyChanged.connect(lambda body_name: self.handle_selected_body_changed(body_name))
        self.view.removeBodySignal.connect(self.handle_remove_body_clicked)
        self.view.addBodySignal.connect(self.handle_add_body_clicked)
        self.view.playPauseSignal.connect(self.handle_play_pause_clicked)

        self.view.reset_view(self.model.initial_body_parameters())

    def handle_selected_body_changed(self, body_name: str) -> None:
        parameters = self.model.parameters(body_name)
        if parameters is not None:
            self.view.set_mass(parameters[0])
            self.view.set_position(parameters[1], parameters[2])

    def handle_remove_body_clicked(self) -> None:
        if self.model.number_of_bodies() > 1:
            body_name = self.view.selected_body()
            self.model.remove_body(body_name)
            self.view.remove_body(body_name)

    def handle_add_body_clicked(self) -> None:
        if self.model.number_of_bodies() < 5:
            self._add_new_body()

    def handle_play_pause_clicked(self) -> None:
        previously_running = self.view.is_simulating()
        self.view.set_as_simulating(not previously_running)

    def _add_new_body(self) -> None:
        body_name, mass, x, y = self.view.open_add_body_dialog()
        if body_name is not None:
            self.model.add_body(body_name, mass, x, y)
            self.view.add_body(body_name, self.model.parameters(body_name))
