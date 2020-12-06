# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import random
import string

from n_body_simulations.error_catcher import catch_errors
from n_body_simulations.xml_reader import get_simulation_setting, get_user_interface_property


class NBodySimulationsPresenter:
    """A class used as a presenter for the main GUI (MVP)."""

    body_colours = get_user_interface_property("body-colours").split(",")
    body_names = get_user_interface_property("body-names").split(",")

    file_verification_stamp = get_user_interface_property("file-verification-stamp")

    max_number_of_bodies = int(get_simulation_setting("max-number-of-bodies"))
    body_mass_default = float(get_simulation_setting("body-mass-default"))
    body_vx_default = float(get_simulation_setting("body-vx-default"))
    body_vy_default = float(get_simulation_setting("body-vy-default"))
    time_step_default = float(get_simulation_setting("time-step-default"))
    duration_default = float(get_simulation_setting("duration-default"))

    def __init__(self, view, model):
        """Initializes the presenter by creating a view and model."""
        self.view = view
        self.model = model

        self.view.subscribe_presenter(self)

        self.model.simulationFinished.connect(self.handle_simulation_finished)
        self.model.simulationError.connect(lambda error_message: self.handle_simulation_error(error_message))

        self.play_clicked = False

        self.model.set_time_step(self.time_step_default)
        self.model.set_duration(self.duration_default)

    def open_widget(self) -> None:
        """Opens the widget in a window."""
        self.view.show()

    def notify_presenter(self, event, *args) -> None:
        """Notify the presenter when an event occurs in the view."""
        handlers = {self.view.ViewEvent.LoadProjectClicked: self.handle_load_project_clicked,
                    self.view.ViewEvent.SaveProjectClicked: self.handle_save_project_clicked,
                    self.view.ViewEvent.RemoveBodyClicked: self.handle_remove_body_clicked,
                    self.view.ViewEvent.AddBodyClicked: self.handle_add_body_clicked,
                    self.view.ViewEvent.AddBodiesClicked: self.handle_add_bodies_clicked,
                    self.view.ViewEvent.TimeStepChanged: self.handle_time_step_changed,
                    self.view.ViewEvent.DurationChanged: self.handle_duration_changed,
                    self.view.ViewEvent.NameChanged: self.handle_body_name_changed,
                    self.view.ViewEvent.MassChanged: self.handle_mass_changed,
                    self.view.ViewEvent.XPositionChanged: self.handle_x_position_changed,
                    self.view.ViewEvent.YPositionChanged: self.handle_y_position_changed,
                    self.view.ViewEvent.VxPositionChanged: self.handle_x_velocity_changed,
                    self.view.ViewEvent.VyPositionChanged: self.handle_y_velocity_changed,
                    self.view.ViewEvent.PlayPauseClicked: self.handle_play_pause_clicked,
                    self.view.ViewEvent.BodyMovedOnPlot: self.handle_body_moved,
                    self.view.ViewEvent.BodyVelocityChangedOnPlot: self.handle_body_velocity_changed}

        handler = handlers.get(event, None)
        if handler is not None:
            if args:
                handler(*args)
            else:
                handler()

    def handle_load_project_clicked(self) -> None:
        """Handles the loading of a project file."""
        file_path = self.view.open_file_dialog_for_loading()
        if file_path is not None:
            self.view.clear()
            self.model.clear()
            self._load_project(file_path)

    @catch_errors()
    def handle_save_project_clicked(self) -> None:
        """Handles the saving of a project."""
        initial_data = self.model.initial_body_parameters()
        if len(initial_data.keys()) > 0:
            file_path = self.view.open_file_dialog_for_saving()
            if file_path is not None:
                self._save_project(file_path, initial_data)
        else:
            raise RuntimeError("Cannot save an empty project.")

    def handle_remove_body_clicked(self) -> None:
        """Handles the removal of the selected bodies."""
        body_names = self.view.selected_bodies()
        if body_names:
            for body_name in body_names:
                self.view.remove_body(body_name)
                self.model.remove_body(body_name)

    def handle_add_body_clicked(self, body_name: str) -> None:
        """Handles the addition of a body to the simulation. Randomizes the body position and colour."""
        if self.model.number_of_bodies() < self.max_number_of_bodies:
            self._add_body(body_name)

    def handle_add_bodies_clicked(self, number_of_bodies: int) -> None:
        """Handles the addition of N random bodies. Randomizes the body position, colour, and name."""
        for _ in range(number_of_bodies):
            self.handle_add_body_clicked(self._generate_new_random_name())

    @catch_errors()
    def handle_body_name_changed(self, old_name: str, new_name: str) -> None:
        """Handles when the name of a body is changed."""
        if new_name not in self.model.body_names():
            self.model.set_name(old_name, new_name)
            self.view.update_body_name(old_name, new_name)
        else:
            self.view.set_name(old_name)
            raise ValueError(f"Could not change body name: The body '{new_name}' already exists.")

    def handle_mass_changed(self, body_name: str, mass: float) -> None:
        """Handles when the mass of a body is changed."""
        self.model.set_mass(body_name, mass)
        self.view.update_body_mass(body_name, mass)

    def handle_x_position_changed(self, body_name: str, x: float) -> None:
        """Handles when the x position of a body is changed."""
        self.model.set_x_position(body_name, x)
        self.view.update_body_position(body_name, self.model.initial_position(body_name))

    def handle_y_position_changed(self, body_name: str, y: float) -> None:
        """Handles when the y position of a body is changed."""
        self.model.set_y_position(body_name, y)
        self.view.update_body_position(body_name, self.model.initial_position(body_name))

    def handle_x_velocity_changed(self, body_name: str, vx: float) -> None:
        """Handles when the x velocity of a body is changed."""
        self.model.set_x_velocity(body_name, vx)
        self.view.update_body_velocity(body_name, self.model.initial_velocity(body_name))

    def handle_y_velocity_changed(self, body_name: str, vy: float) -> None:
        """Handles when the y velocity of a body is changed."""
        self.model.set_y_velocity(body_name, vy)
        self.view.update_body_velocity(body_name, self.model.initial_velocity(body_name))

    def handle_time_step_changed(self, time_step: float) -> None:
        """Handles when the time step is changed."""
        self.model.set_time_step(time_step)

    def handle_duration_changed(self, duration: float) -> None:
        """Handles when the duration is changed."""
        self.model.set_duration(duration)

    def handle_play_pause_clicked(self) -> None:
        """Handles when the play/pause button is clicked."""
        self.play_clicked = not self.view.is_simulating()
        self.view.set_as_playing(self.play_clicked)

        if self.play_clicked and self.model.has_data_changed():
            self.view.stop_simulation()
            self.view.enable_view(False)
            self.model.start()
        elif self.play_clicked:
            self.view.play_simulation()
        else:
            self.view.pause_simulation()

    def handle_body_moved(self, body_name: str, x: float, y: float) -> None:
        """Handles when the body has been moved on the interactive plot."""
        self.model.set_x_position(body_name, x)
        self.model.set_y_position(body_name, y)

    def handle_body_velocity_changed(self, body_name: str, vx: float, vy: float) -> None:
        """Handles when a bodies velocity has been changed on the interactive plot."""
        self.model.set_x_velocity(body_name, vx)
        self.model.set_y_velocity(body_name, vy)

    def handle_simulation_finished(self) -> None:
        """Handles when the simulation thread finishes."""
        self.view.enable_view(True)
        self.view.start_simulation(self.model.simulation_results())

        if self.play_clicked:
            self.view.play_simulation()
        else:
            self.view.pause_simulation()

    @catch_errors()
    def handle_simulation_error(self, error_message: str) -> None:
        """Handles when an error occurs during a simulation."""
        self.view.enable_view(True)
        self.view.set_as_playing(False)
        raise RuntimeError(error_message)

    @catch_errors()
    def _load_project(self, file_path: str) -> None:
        """Loads the body data from a .txt file."""
        with open(file_path, "r") as file:
            file_lines = list(filter(None, file.read().split("\n")))
            if file_lines[0] == self.file_verification_stamp:
                first_line_split = file_lines[1].split(" ")
                self._load_project_data(float(first_line_split[0]), float(first_line_split[1]), file_lines[2:])
            else:
                raise RuntimeError(f"The file verification stamp at the start of this file is incorrect. "
                                   f"It should say:\n'{self.file_verification_stamp}'.")

    def _load_project_data(self, time_step: float, duration: float, initial_data: list) -> None:
        """Loads body data into the view and model."""
        self._set_time_step(time_step)
        self._set_duration(duration)
        self.view.reset_plot_options()

        for line in initial_data:
            line_split = line.split(" ")
            self._add_new_body(line_split[0], line_split[1], float(line_split[2]), float(line_split[3]),
                               float(line_split[4]), float(line_split[5]), float(line_split[6]))

    def _save_project(self, file_path: str, initial_data: dict) -> None:
        """Saves the body data into a .txt file."""
        lines = [f"{self.file_verification_stamp}\n", f"{self.model.time_step()} {self.model.duration()}\n"]
        for body_name, initial_data in initial_data.items():
            colour = self.view.get_body_colour(body_name)
            mass, position, velocity = initial_data[0], initial_data[1], initial_data[2]
            lines.append(f"{colour} {body_name} {mass} {position.x} {position.y} {velocity.x} {velocity.y}\n")

        with open(file_path, "w") as file:
            file.writelines(lines)

    def _set_time_step(self, time_step: float) -> None:
        """Set the time step of the simulation in the view and model."""
        self.view.set_time_step(time_step)
        self.model.set_time_step(time_step)

    def _set_duration(self, duration: float) -> None:
        """Set the duration of the simulation in the view and model."""
        self.view.set_duration(duration)
        self.model.set_duration(duration)

    def _add_body(self, body_name: str) -> None:
        """Adds a new body with a random position to the model and view."""
        if body_name != "":
            axes_limits = self.view.get_axes_limits()
            x = random.uniform(axes_limits[0], axes_limits[1])
            y = random.uniform(axes_limits[2], axes_limits[3])
            self._add_new_body(self._random_colour(), body_name, self.body_mass_default, x, y, self.body_vx_default,
                               self.body_vy_default)

    def _add_new_body(self, colour: str, body_name: str, mass: float, x: float, y: float, vx: float, vy: float) -> None:
        """Adds a new body to the model and view."""
        if body_name != "" and self.model.add_body(body_name, mass, x, y, vx, vy):
            self.view.add_body(colour, body_name, self.model.initial_data(body_name))

    def _random_colour(self) -> str:
        """Returns a random colour to be used for a body."""
        return self.body_colours[random.randint(0, len(self.body_colours) - 1)]

    def _generate_new_random_name(self) -> str:
        """Keeps generating a random name until an unused name is found."""
        random_name = self._generate_random_name()
        while random_name in self.model.body_names():
            random_name = self._generate_random_name()
        return random_name

    def _generate_random_name(self) -> str:
        """Generates a random body name."""
        random_name = self.body_names[random.randint(0, len(self.body_names) - 1)]
        random_number = random.randint(1, 100)
        random_letter = random.choice(string.ascii_uppercase)
        return f"{random_name}-{random_number}{random_letter}"
