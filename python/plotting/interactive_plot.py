# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.simulation_animator import SimulationAnimator
from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

AXIS_MARGIN = 0.05  # 5% axis margin
LINESTYLE = " "
MARKER = '.'


class InteractivePlot:
    """A class used for the interactive plot displaying the simulation data."""

    def __init__(self):
        """Initialize the interactive plot."""
        self._figure = Figure()
        # Modify margins around a figure
        self._figure.subplots_adjust(left=0.2, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)
        self._figure.patch.set_facecolor('#f0f0f0')
        self._ax = self._figure.add_subplot(111)
        self._ax.set_autoscale_on(True)
        self._canvas = FigureCanvas(self._figure)

        self._lines = dict()
        self._initial_data = dict()

        self._animator = SimulationAnimator(self._figure)

    def canvas(self) -> FigureCanvas:
        """Returns the canvas used for the interactive plot."""
        return self._canvas

    def clear(self) -> None:
        """Clears the interactive plot."""
        self._ax.clear()
        self._lines.clear()

    def remove_body(self, body_name: str) -> None:
        """Removes a body from the interactive plot."""
        if body_name in self._lines:
            self._lines[body_name].remove()
            del self._lines[body_name]
            del self._initial_data[body_name]

    def add_body(self, body_name: str, position: Vector2D) -> None:
        """Adds a body to the interactive plot."""
        lines = self._ax.plot(position.x, position.y, label=body_name, marker=MARKER, linestyle=LINESTYLE)
        self._lines[body_name] = lines[0]

        self._initial_data[body_name] = position

    def set_simulation_data(self, simulation_data: dict) -> None:
        """Sets the simulation data in the animator."""
        self._animator.set_simulation_data(simulation_data)

    def disable_animation(self) -> None:
        """Disables the animator and re-plots the bodies in their initial positions."""
        self._animator.disable()
        self._initialize_bodies()

    def start_animation(self) -> None:
        """Starts the animation for the first time."""
        self._animator.start(self._lines)
        self.show_legend()
        self.draw()

    def stop_animation(self) -> None:
        """Stops the animation."""
        self._animator.stop()

    def pause_animation(self) -> None:
        """Pauses the animation."""
        self._animator.pause()

    def play_animation(self) -> None:
        """Plays the animation."""
        if self._animator.is_enabled():
            self._animator.play()
        else:
            self.start_animation()

    def show_legend(self) -> None:
        """Shows the legend if there are lines on the plot."""
        if len(self._lines) > 0:
            self._ax.legend()

    def draw(self) -> None:
        """Draws the lines onto the canvas."""
        self._canvas.draw()

    def update_axes_limits(self, initial_data: bool = True) -> None:
        """Re-sizes the axis limits for the plot based on the initial data or simulation data."""
        if initial_data:
            x_min, x_max, y_min, y_max = self._calculate_initial_axes_min_max()
        else:
            x_min, x_max, y_min, y_max = self._calculate_simulation_axes_min_max()

        if x_min == x_max:
            x_min -= 0.5
            x_max += 0.5

        if y_min == y_max:
            y_min -= 0.5
            y_max += 0.5

        x_margin = (x_max-x_min)*AXIS_MARGIN
        y_margin = (y_max-y_min)*AXIS_MARGIN

        self._ax.set_xlim(x_min - x_margin, x_max + x_margin)
        self._ax.set_ylim(y_min - y_margin, y_max + y_margin)

    def _calculate_initial_axes_min_max(self) -> tuple:
        """Calculates the min-max of both axes based on the initial body data."""
        xs, ys = [], []
        for position in self._initial_data.values():
            xs.append(position.x)
            ys.append(position.y)
        return min(xs), max(xs), min(ys), max(ys)

    def _calculate_simulation_axes_min_max(self) -> tuple:
        """Calculates the min-max of both axes based on the simulated body data."""
        xs, ys = [], []
        for body_positions in self._animator.simulation_data().values():
            for position in body_positions.values():
                xs.append(position.x)
                ys.append(position.y)
        return min(xs), max(xs), min(ys), max(ys)

    def _initialize_bodies(self) -> None:
        """Re-plots the bodies using their initial positions."""
        for body_name, position in self._initial_data.items():
            self.remove_body(body_name)
            self.add_body(body_name, position)

        self.show_legend()
        self.draw()
