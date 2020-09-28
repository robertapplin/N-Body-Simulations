# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from qt.model import NBodySimulationsModel


class NBodySimulationsPresenter:

    def __init__(self, view):
        self.view = view
        self.model = NBodySimulationsModel()

        self.view.removeBodySignal.connect(self.handle_remove_body_clicked)
        self.view.addBodySignal.connect(self.handle_add_body_clicked)
        self.view.playPauseSignal.connect(self.handle_play_pause_clicked)

        self.view.reset_view(self.model.initial_body_parameters())

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
        new_body = self.view.open_add_body_dialog()
        if new_body is not None:
            self.model.add_body(new_body)
            self.view.add_body(new_body, self.model.position(new_body))
