# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

ANIMATION_INTERVAL = 3
MARKER = '.'


class SimulationAnimator:
    """A class used for animating the simulation data."""

    def __init__(self, figure: FigureCanvas):
        """Initialize the animator using the InteractivePlot figure."""
        self._figure = figure
        self._animation = None

        self._lines = dict()
        self._simulation_data = dict()
        self._t = 0.0

        self._playing = False
        self._active = False

    def disable(self) -> None:
        """Stops the animation and disables the animator so that the InteractivePlot can be used."""
        self._active = False
        self.stop()
        if self._animation:
            self._animation.event_source.stop()

    def enable(self, lines: dict) -> None:
        """Enables the animator and starts animating the simulation data."""
        if self._active:
            self.disable()

        self._active = True
        self._lines = lines
        self._animation = FuncAnimation(self._figure, self._update_body_positions, self._time,
                                        interval=ANIMATION_INTERVAL)

    def is_enabled(self) -> bool:
        """Returns whether the animator is active or not."""
        return self._active

    def set_simulation_data(self, simulation_data: dict) -> None:
        """Sets the simulation data to be animated."""
        self._simulation_data = simulation_data

    def simulation_data(self) -> dict:
        """Returns the simulation data currently being animated."""
        return self._simulation_data

    def start(self, lines: dict) -> None:
        """Starts the animation for the first time."""
        self.enable(lines)
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

    def time_step(self) -> float:
        """Returns the time step used for the simulation."""
        times = list(list(self._simulation_data.values())[0].keys())
        return abs(times[-1] / (len(times) - 1))

    def duration(self) -> float:
        """Returns the duration of the simulation."""
        return list(list(self._simulation_data.values())[0].keys())[-1]

    def _update_body_positions(self, time: float) -> dict:
        """Updates the positions of the bodies in the animation."""
        for body_name, positions in self._simulation_data.items():
            self._lines[body_name].set_xdata(positions[time].x)
            self._lines[body_name].set_ydata(positions[time].y)
        return self._lines

    def _time(self) -> float:
        """A generator for stepping through each time step for the simulation."""
        self._t = 0.0
        t_max = self.duration()
        time_step = self.time_step()

        while self._t < t_max:
            if self._playing:
                self._t += time_step
            yield self._t
