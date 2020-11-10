# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.body_marker import BodyMarker
from n_body_simulations.simulation_animator import SimulationAnimator
from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QApplication

AXIS_MARGIN = 0.05  # 5% axis margin


class InteractivePlot(QObject):
    """A class used for the interactive plot displaying the simulation data."""
    bodyMovedSignal = pyqtSignal(str, float, float)

    def __init__(self):
        """Initialize the interactive plot."""
        super(InteractivePlot, self).__init__()

        self._figure = Figure()

        # Modify margins around a figure
        self._figure.subplots_adjust(left=0.015, bottom=0.015, right=0.985, top=0.985, wspace=0, hspace=0)
        self._figure.patch.set_facecolor("#f0f0f0")

        self._ax = self._figure.add_subplot(111)
        self._ax.set_autoscale_on(True)
        self._canvas = FigureCanvas(self._figure)

        # Make the figure square
        self._figure.gca().set_aspect("equal", adjustable="box")

        self._ax.get_xaxis().set_visible(False)
        self._ax.get_yaxis().set_visible(False)

        self.mouse_move_connection = self._figure.canvas.mpl_connect("motion_notify_event", self.handle_mouse_event)
        self.mouse_press_connection = self._figure.canvas.mpl_connect("button_press_event", self.handle_mouse_event)
        self.mouse_release_connection = self._figure.canvas.mpl_connect("button_release_event", self.handle_mouse_event)

        self._event_switcher = {"motion_notify_event": self.handle_mouse_moved,
                                "button_press_event": self.handle_mouse_pressed,
                                "button_release_event": self.handle_mouse_released}

        self._body_markers = dict()
        self._initial_data = dict()
        self._axes_resized = False

        self._animator = SimulationAnimator(self._figure)

    def handle_mouse_event(self, event: QMouseEvent) -> None:
        """Handles mouse events such as movement, pressing and releasing the mouse button."""
        x, y = event.xdata, event.ydata
        if x is not None and y is not None:
            event_handler = self._event_switcher.get(event.name, None)
            if event_handler is not None:
                event_handler(x, y)
                self._update_cursor()

    def handle_mouse_moved(self, x: float, y: float) -> None:
        """Handles the mouse movement event. Redraw if a body marker was dragged."""
        for body_marker in self._body_markers.values():
            redraw = body_marker.mouse_moved(x, y)
            if redraw:
                self._canvas.draw()
                break

    def handle_mouse_pressed(self, x: float, y: float) -> None:
        """Handles the mouse press event. If the dragging of a body starts, stop checking the other bodies."""
        for body_marker in self._body_markers.values():
            drag_started = body_marker.mouse_drag_start(x, y)
            if drag_started:
                break

    def handle_mouse_released(self, x: float, y: float) -> None:
        """Handles the mouse release event. Redraw if a body marker has been moved for the final time."""
        for body_marker in self._body_markers.values():
            redraw = body_marker.mouse_drag_stop(x, y)
            if redraw:
                self._canvas.draw()
                break

    def handle_body_moved(self, body_name: str, x: float, y: float) -> None:
        """Handles when a body has been moved on the interactive plot."""
        self._initial_data[body_name] = Vector2D(x, y)
        self.bodyMovedSignal.emit(body_name, x, y)

    def canvas(self) -> FigureCanvas:
        """Returns the canvas used for the interactive plot."""
        return self._canvas

    def clear(self) -> None:
        """Clears the interactive plot."""
        self._ax.clear()
        self._body_markers.clear()

    def remove_body(self, body_name: str) -> None:
        """Removes a body from the interactive plot."""
        if body_name in self._body_markers:
            self._body_markers[body_name].remove_body()
            del self._body_markers[body_name]
            del self._initial_data[body_name]

    def add_body(self, body_name: str, position: Vector2D, colour: str) -> None:
        """Adds a body to the interactive plot."""
        self._body_markers[body_name] = BodyMarker(self._canvas, body_name, position, colour)
        self._body_markers[body_name].bodyMovedSignal.connect(lambda name, x, y: self.handle_body_moved(name, x, y))

        self._initial_data[body_name] = position

    def set_simulation_data(self, simulation_data: dict) -> None:
        """Sets the simulation data in the animator."""
        self._animator.set_simulation_data(simulation_data)

    def disable_animation(self) -> None:
        """Disables the animator and re-plots the bodies in their initial positions."""
        if self._animator.is_enabled():
            self.mouse_move_connection = self._figure.canvas.mpl_connect("motion_notify_event", self.handle_mouse_event)
            self.mouse_press_connection = self._figure.canvas.mpl_connect("button_press_event", self.handle_mouse_event)
            self.mouse_release_connection = self._figure.canvas.mpl_connect("button_release_event", self.handle_mouse_event)

            self._animator.disable()
            self._initialize_bodies()

    def start_animation(self) -> None:
        """Starts the animation for the first time."""
        self._canvas.mpl_disconnect(self.mouse_move_connection)
        self._canvas.mpl_disconnect(self.mouse_press_connection)
        self._canvas.mpl_disconnect(self.mouse_release_connection)

        self._animator.start(self._body_markers)
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

    def draw(self) -> None:
        """Draws the lines onto the canvas."""
        if self._axes_resized:
            self._refresh_body_markers()
            self._axes_resized = False
        self._canvas.draw()

    def get_axes_limits(self) -> tuple:
        """Returns the axes limits currently being used for the plot (minus the margin)."""
        x_min, x_max = self._ax.get_xlim()
        y_min, y_max = self._ax.get_ylim()

        x_diff = abs(x_max - x_min)
        y_diff = abs(y_max - y_min)

        x_margin = (x_diff * AXIS_MARGIN) / (1 + 2 * AXIS_MARGIN)
        y_margin = (y_diff * AXIS_MARGIN) / (1 + 2 * AXIS_MARGIN)

        return tuple([x_min + x_margin, x_max - x_margin, y_min + y_margin, y_max - y_margin])

    def update_body_colour(self, body_name: str, colour: str) -> None:
        """Updates the colour of a body to a new colour."""
        self._body_markers[body_name].set_colour(colour)
        self._body_markers[body_name].refresh()

    def update_body_name(self, old_name: str, new_name: str) -> None:
        """Updates the name of a body to a new name."""
        if old_name in self._body_markers:
            self._body_markers[new_name] = self._body_markers[old_name]
            del self._body_markers[old_name]

            self._initial_data[new_name] = self._initial_data[old_name]
            del self._initial_data[old_name]

    def update_axes_limits(self, initial_data: bool = True) -> None:
        """Re-sizes the axis limits for the plot based on the initial data or simulation data."""
        if initial_data:
            x_min, x_max, y_min, y_max = self._calculate_initial_axes_min_max()
        else:
            x_min, x_max, y_min, y_max = self._calculate_simulation_axes_min_max()

        x_half_diff = abs(x_max - x_min) / 2.0
        y_half_diff = abs(y_max - y_min) / 2.0
        x_mid = x_min + x_half_diff
        y_mid = y_min + y_half_diff

        if x_half_diff > y_half_diff:
            y_min = y_mid - x_half_diff
            y_max = y_mid + x_half_diff
        elif x_half_diff < y_half_diff:
            x_min = x_mid - y_half_diff
            x_max = x_mid + y_half_diff
        else:
            x_min -= 0.5
            x_max += 0.5
            y_min -= 0.5
            y_max += 0.5

        x_margin = (x_max-x_min)*AXIS_MARGIN
        y_margin = (y_max-y_min)*AXIS_MARGIN

        self._ax.set_xlim(x_min - x_margin, x_max + x_margin)
        self._ax.set_ylim(y_min - y_margin, y_max + y_margin)

        self._axes_resized = True

    def _calculate_initial_axes_min_max(self) -> tuple:
        """Calculates the min-max of both axes based on the initial body data."""
        xs, ys = [], []
        for position in self._initial_data.values():
            xs.append(position.x)
            ys.append(position.y)

        if len(xs) == 0:
            xs = [0.0]
        if len(ys) == 0:
            ys = [0.0]

        return min(xs), max(xs), min(ys), max(ys)

    def _calculate_simulation_axes_min_max(self) -> tuple:
        """Calculates the min-max of both axes based on the simulated body data."""
        xs, ys = [], []
        for body_positions in self._animator.simulation_data().values():
            for position in body_positions.values():
                xs.append(position.x)
                ys.append(position.y)

        if len(xs) == 0:
            xs = [0.0]
        if len(ys) == 0:
            ys = [0.0]

        return min(xs), max(xs), min(ys), max(ys)

    def _refresh_body_markers(self) -> None:
        """Updates the size of the bodies just before a draw event."""
        self._canvas.draw()
        for body_marker in self._body_markers.values():
            body_marker.refresh()

    def _initialize_bodies(self) -> None:
        """Re-plots the bodies using their initial positions."""
        for body_name, position in self._initial_data.items():
            colour = self._body_markers[body_name].get_colour()
            self.remove_body(body_name)
            self.add_body(body_name, position, colour)

        self.draw()

    def _update_cursor(self) -> None:
        """Updates the cursor based on the mouse events being performed."""
        cursor = Qt.ArrowCursor
        for body_marker in self._body_markers.values():
            override_cursor = body_marker.get_override_cursor()
            if override_cursor is not None:
                cursor = override_cursor
                if cursor == Qt.ClosedHandCursor:
                    break
        self._set_override_cursor(cursor)

    @staticmethod
    def _set_override_cursor(cursor: QCursor) -> None:
        """Sets the cursor being used."""
        if QApplication.overrideCursor() != cursor:
            QApplication.restoreOverrideCursor()
            QApplication.setOverrideCursor(cursor)
