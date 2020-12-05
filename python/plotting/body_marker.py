# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.patches import Circle, FancyArrow, Patch

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QCursor

ARROW_HEAD_WIDTH_PIXELS = 7
BODY_LABEL_SPACING_PIXELS = 5
FONT_SIZE = 9
MARKER_SENSITIVITY = 5
MINIMUM_ARROW_SIZE_PIXELS = 12


class BodyMarker(QObject):
    """A class used for creating a marker to represent a body on the interactive plot."""
    bodyMovedSignal = pyqtSignal(str, float, float)
    bodyVelocityChangedSignal = pyqtSignal(str, float, float)

    def __init__(self, canvas: FigureCanvas, colour: str, name: str, mass: float, position: Vector2D,
                 velocity: Vector2D):
        """Initializes the body marker with a patch and a coordinate label."""
        super(BodyMarker, self).__init__()

        self._canvas = canvas
        self._axis = self._canvas.figure.get_axes()[0]

        self._colour = colour
        self._name = name
        self._mass = mass
        self._position = position
        self._velocity = velocity

        self._body_patch = None
        self._velocity_patch = None
        self._position_label = None
        self._override_cursor = None

        self._velocity_magnification = 1
        self._show_position_label = True
        self._show_velocity_arrow = True

        self._is_dragging_body = False
        self._is_dragging_velocity = False

        self.create_body()

    def mouse_drag_start(self, x: float, y: float) -> bool:
        """Checks if a mouse drag event has started on this body marker. If yes, the override cursor is changed."""
        self._is_dragging_body = self._is_above(x, y, self._position.x, self._position.y)
        if self._is_dragging_body:
            self._set_override_cursor(x, y)
            return True

        if self._show_velocity_arrow:
            self._is_dragging_velocity = \
                self._is_above(x, y, self._position.x + self._velocity.x * self._velocity_magnification,
                               self._position.y + self._velocity.y * self._velocity_magnification)
            if self._is_dragging_velocity:
                self._set_override_cursor(x, y)
                return True

        return False

    def mouse_drag_stop(self, x: float, y: float) -> bool:
        """Checks if a mouse drag event has stopped for this body marker. If yes, the override cursor is changed."""
        if self._is_dragging_body:
            self.set_position(x, y)
            self._is_dragging_body = False
            self._set_override_cursor(x, y)
            return True

        if self._show_velocity_arrow and self._is_dragging_velocity:
            self.set_velocity((x - self._position.x) / self._velocity_magnification,
                              (y - self._position.y) / self._velocity_magnification)
            self._is_dragging_velocity = False
            self._set_override_cursor(x, y)
            return True

        return False

    def mouse_moved(self, x: float, y: float) -> bool:
        """Checks if this body marker is being dragged. If yes, then the position of the body marker is updated."""
        self._set_override_cursor(x, y)

        if self._is_dragging_body:
            self.set_position(x, y)
            return True

        if self._show_velocity_arrow and self._is_dragging_velocity:
            self.set_velocity((x - self._position.x) / self._velocity_magnification,
                              (y - self._position.y) / self._velocity_magnification)
            return True

        return False

    def remove_body(self) -> None:
        """Removes the body marker from the interactive plot."""
        self._body_patch.remove()
        if self._velocity_patch is not None:
            self._velocity_patch.remove()
        if self._position_label is not None:
            self._position_label.remove()

    def create_body(self) -> None:
        """Creates the body marker, velocity arrow, and position label."""
        self._create_position_label()
        self._create_velocity_arrow()
        self._create_position_circle()

    def show_body(self, show_body: bool) -> None:
        """Show or hide the body on the interactive plot. It is hidden if it merges with another body."""
        self._body_patch.set_visible(show_body)
        self._position_label.set_visible(show_body)
        self._velocity_patch.set_visible(show_body)

    def show_position_label(self, show_label: bool) -> None:
        """Show or hide the position label on the interactive plot."""
        self._show_position_label = show_label
        self._position_label.set_visible(show_label)

    def show_velocity_arrow(self, show_velocity: bool) -> None:
        """Show or hide the velocity arrow on the interactive plot."""
        self._show_velocity_arrow = show_velocity
        self._velocity_patch.set_visible(self._is_velocity_arrow_above_minimum() and show_velocity)

    def set_velocity_arrow_magnification(self, magnification: int) -> None:
        """Set the magnification of the velocity arrow."""
        self._velocity_magnification = magnification

    def refresh(self) -> None:
        """Refreshes the body marker. This is required to reset its size and colour."""
        self.remove_body()
        self.create_body()

    def set_colour(self, colour: str) -> None:
        """Sets the colour used for this body marker."""
        self._colour = colour

    def get_colour(self) -> str:
        """Returns the colour used for this body marker."""
        return self._colour

    def set_mass(self, mass: float, recreate_body: bool = True) -> None:
        """Sets the mass of a body marker."""
        self._mass = mass

        if recreate_body:
            self.remove_body()
            self.create_body()

    def set_position(self, x: float, y: float, emit_signal: bool = True, recreate_body: bool = True) -> None:
        """Sets a new position for this body marker, and emits a signal."""
        self._position = Vector2D(x, y)

        if recreate_body:
            self.remove_body()
            self.create_body()

        if emit_signal:
            self.bodyMovedSignal.emit(self._name, x, y)

    def set_velocity(self, vx: float, vy: float, emit_signal: bool = True, recreate_body: bool = True) -> None:
        """Sets a new velocity for this body marker, and emits a signal."""
        self._velocity = Vector2D(vx, vy)

        if recreate_body:
            self.remove_body()
            self.create_body()

        if emit_signal:
            self.bodyVelocityChangedSignal.emit(self._name, vx, vy)

    def get_body_patch(self) -> Patch:
        """Returns the patch which represents the body marker."""
        return self._body_patch

    def get_velocity_patch(self) -> Patch:
        """Returns the patch which represents the velocity of the body."""
        return self._velocity_patch

    def get_override_cursor(self) -> QCursor:
        """Returns the override cursor currently set for this body marker."""
        return self._override_cursor

    def _create_velocity_arrow(self) -> None:
        """Creates the velocity arrow if necessary."""
        self._velocity_patch = FancyArrow(self._position.x, self._position.y,
                                          self._velocity.x * self._velocity_magnification,
                                          self._velocity.y * self._velocity_magnification, length_includes_head=True,
                                          facecolor=self._colour, edgecolor="black",
                                          head_width=self._pixels_to_distance(ARROW_HEAD_WIDTH_PIXELS))
        self._axis.add_patch(self._velocity_patch)

        self._velocity_patch.set_visible(self._is_velocity_arrow_above_minimum() and self._show_velocity_arrow)

    def _create_position_circle(self) -> None:
        """Creates a circle used to mark the position of a body."""
        self._body_patch = Circle((self._position.x, self._position.y), self._pixels_to_distance(self._body_radius()),
                                  facecolor=self._colour)
        self._axis.add_patch(self._body_patch)

    def _create_position_label(self) -> None:
        """Creates the label that denotes the position of a body."""
        label_position = (self._position.x + self._pixels_to_distance(BODY_LABEL_SPACING_PIXELS), self._position.y)
        self._position_label = self._axis.annotate(f"({self._position.x:.2f},{self._position.y:.2f})", label_position,
                                                   fontsize=FONT_SIZE)
        self._position_label.set_visible(self._show_position_label)

    def _set_override_cursor(self, x_mouse: float, y_mouse: float) -> None:
        """Sets the override cursor for this body marker."""
        if self._is_dragging_body or self._is_dragging_velocity:
            self._override_cursor = Qt.ClosedHandCursor
        elif not self._is_dragging_body and self._is_above(x_mouse, y_mouse, self._position.x, self._position.y):
            self._override_cursor = Qt.OpenHandCursor
        elif self._show_velocity_arrow and not self._is_dragging_velocity and \
                self._is_above(x_mouse, y_mouse, self._position.x + self._velocity.x * self._velocity_magnification,
                               self._position.y + self._velocity.y * self._velocity_magnification):
            self._override_cursor = Qt.OpenHandCursor
        else:
            self._override_cursor = None

    def _body_radius(self) -> int:
        """Returns the body radius to use in pixels."""
        if self._mass <= 0.0001:
            return 2
        elif self._mass <= 0.001:
            return 3
        elif self._mass <= 0.01:
            return 4
        elif self._mass <= 0.1:
            return 5
        elif self._mass <= 1.0:
            return 6
        elif self._mass <= 10.0:
            return 7
        return 8

    def _is_velocity_arrow_above_minimum(self) -> bool:
        """Returns true if the velocity arrow is large enough to be plotted."""
        return (self._distance_to_pixels(self._velocity.magnitude() * self._velocity_magnification)
                >= MINIMUM_ARROW_SIZE_PIXELS)

    def _is_above(self, x_mouse: float, y_mouse: float, x_to_check: float, y_to_check: float) -> bool:
        """Returns true if the mouse position is above the given x and y position."""
        mouse_x_pixels, mouse_y_pixels = self._axis.transData.transform((x_mouse, y_mouse))
        x_pixels, y_pixels = self._axis.transData.transform((x_to_check, y_to_check))

        r_pixels = ((mouse_x_pixels - x_pixels)**2 + (mouse_y_pixels - y_pixels)**2)**(1/2)

        return r_pixels < MARKER_SENSITIVITY

    def _pixels_to_distance(self, pixels: int) -> float:
        """Converts a pixel size to a axes distance size."""
        x1, _ = self._axis.transData.inverted().transform((0, 0))
        x2, _ = self._axis.transData.inverted().transform((pixels, 0))
        return x2 - x1

    def _distance_to_pixels(self, distance: float) -> float:
        """Converts a axes distance size to a pixel size."""
        x1, _ = self._axis.transData.transform((0, 0))
        x2, _ = self._axis.transData.transform((distance, 0))
        return x2 - x1
