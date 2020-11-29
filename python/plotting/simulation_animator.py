# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml_reader import get_user_interface_property

from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SimulationAnimator:
    """A class used for animating the simulation data."""

    time_dp = int(get_user_interface_property("time-dp"))

    def __init__(self, figure: FigureCanvas):
        """Initialize the animator using the InteractivePlot figure."""
        self._figure = figure
        self._animation = None
        self._animation_interval = int(get_user_interface_property("frame-delay-default"))

        self._body_markers = dict()

        # Dict("Body Name": Dict(Time: Position))
        self._position_data = dict()
        # Dict("Body Name": Dict(Time: Velocity))
        self._velocity_data = dict()

        self._t = 0.0

        self._playing = False
        self._active = False

    def disable(self) -> None:
        """Stops the animation and disables the animator so that the InteractivePlot can be used."""
        self._active = False
        self.stop()
        if self._animation:
            self._animation.event_source.stop()

    def enable(self, body_markers: dict) -> None:
        """Enables the animator and starts animating the simulation data."""
        if self._active:
            self.disable()

        self._active = True
        self._body_markers = body_markers
        self._animation = FuncAnimation(self._figure, self._update_bodies, self._time,
                                        interval=self._animation_interval)

    def is_enabled(self) -> bool:
        """Returns whether the animator is active or not."""
        return self._active

    def set_animation_interval(self, interval: int) -> None:
        """Set the frame delay of the animation in milliseconds."""
        self._animation_interval = interval

    def set_simulation_data(self, simulation_data: tuple) -> None:
        """Sets the simulated position and velocity data to be animated."""
        self._position_data = simulation_data[0]
        self._velocity_data = simulation_data[1]
        self._update_time_step()
        self._update_duration()

    def positional_data(self) -> dict:
        """Returns the simulated positional data currently being animated."""
        return self._position_data

    def start(self, body_markers: dict) -> None:
        """Starts the animation for the first time."""
        self.enable(body_markers)
        self.play()

    def stop(self) -> None:
        """Stops the animation."""
        self._playing = False
        self._t = 0.0

    def pause(self) -> None:
        """Pauses the animation."""
        self._playing = False

    def play(self) -> None:
        """Plays the animation."""
        self._playing = True

    def _update_time_step(self) -> None:
        """Updates the time step of the simulation."""
        times = list(list(self._position_data.values())[0].keys())
        self._time_step = round(abs(times[-1] / (len(times) - 1)), self.time_dp)

    def _update_duration(self) -> float:
        """Returns the duration of the simulation."""
        self._duration = round(list(list(self._position_data.values())[0].keys())[-1], self.time_dp)

    def _update_bodies(self, time: float) -> dict:
        """Updates the positions and velocities of the bodies in the animation."""
        patches = self._update_body_velocities(time)
        patches.extend(self._update_body_positions(time))
        return patches

    def _update_body_positions(self, time: float) -> list:
        """Updates the positions of the bodies in the animation."""
        patches = []
        for body_name, positions in self._position_data.items():
            self._body_markers[body_name].set_position(positions[time].x, positions[time].y, emit_signal=False)
            patches.append(self._body_markers[body_name].get_body_patch())
        return patches

    def _update_body_velocities(self, time: float) -> list:
        """Updates the velocities of the bodies in the animation."""
        patches = []
        for body_name, velocities in self._velocity_data.items():
            self._body_markers[body_name].set_velocity(velocities[time].x, velocities[time].y, emit_signal=False)
            velocity_patch = self._body_markers[body_name].get_velocity_patch()
            if velocity_patch is not None:
                patches.append(velocity_patch)
        return patches

    def _time(self) -> float:
        """A generator for stepping through each time step for the simulation."""
        self._t = 0.0

        while self._t < self._duration:
            if self._playing:
                self._t += self._time_step
            yield round(self._t, self.time_dp)
