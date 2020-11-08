# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.patches import Circle, Patch

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QCursor

BODY_RADIUS_PIXELS = 3
BODY_LABEL_SPACING_PIXELS = 5
MARKER_SENSITIVITY = 5


class BodyMarker(QObject):
    """A class used for creating a marker to represent a body on the interactive plot."""
    bodyMovedSignal = pyqtSignal(str, float, float)

    def __init__(self, canvas: FigureCanvas, name: str, position: Vector2D, colour: str):
        """Initializes the body marker with a patch and a coordinate label."""
        super(BodyMarker, self).__init__()

        self._canvas = canvas
        self._axis = self._canvas.figure.get_axes()[0]

        self._name = name
        self._position = position
        self._colour = colour

        self._patch = None
        self._coordinate_label = None
        self._override_cursor = None
        self._is_dragging = False

        self.create_body()

    def mouse_drag_start(self, x: float, y: float) -> bool:
        """Checks if a mouse drag event has started on this body marker. If yes, the override cursor is changed."""
        self._is_dragging = self._is_above(x, y)
        if self._is_dragging:
            self._set_override_cursor(x, y)
            return True
        return False

    def mouse_drag_stop(self, x: float, y: float) -> bool:
        """Checks if a mouse drag event has stopped for this body marker. If yes, the override cursor is changed."""
        if self._is_dragging:
            self.set_position(x, y)
            self._is_dragging = False
            self._set_override_cursor(x, y)
            return True
        return False

    def mouse_moved(self, x: float, y: float) -> bool:
        """Checks if this body marker is being dragged. If yes, then the position of the body marker is updated."""
        self._set_override_cursor(x, y)
        if self._is_dragging:
            self.set_position(x, y)
            return True
        return False

    def remove_body(self) -> None:
        """Removes the body marker from the interactive plot."""
        self._patch.remove()
        self._coordinate_label.remove()

    def create_body(self) -> None:
        """Creates the body marker and its coordinate label."""
        self._patch = Circle((self._position.x, self._position.y), self._pixels_to_distance(BODY_RADIUS_PIXELS),
                             facecolor=self._colour)
        self._axis.add_patch(self._patch)

        label_position = (self._position.x + self._pixels_to_distance(BODY_LABEL_SPACING_PIXELS), self._position.y)
        self._coordinate_label = self._axis.annotate(f"({self._position.x:.2f},{self._position.y:.2f})", label_position)

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

    def set_position(self, x: float, y: float, emit_signal: bool = True) -> None:
        """Sets a new position for this body marker, and emits a signal."""
        self.remove_body()
        self._position = Vector2D(x, y)
        self.create_body()

        if emit_signal:
            self.bodyMovedSignal.emit(self._name, x, y)

    def get_patch(self) -> Patch:
        """Returns the patch which represents the body marker."""
        return self._patch

    def get_override_cursor(self) -> QCursor:
        """Returns the override cursor currently set for this body marker."""
        return self._override_cursor

    def _set_override_cursor(self, x: float, y: float) -> None:
        """Sets the override cursor for this body marker."""
        if self._is_dragging:
            self._override_cursor = Qt.ClosedHandCursor
        elif not self._is_dragging and self._is_above(x, y):
            self._override_cursor = Qt.OpenHandCursor
        else:
            self._override_cursor = None

    def _is_above(self, x: float, y: float) -> bool:
        """Returns true if the given coordinate is above the current body marker."""
        mouse_x_pixels, mouse_y_pixels = self._axis.transData.transform((x, y))
        body_x_pixels, body_y_pixels = self._axis.transData.transform((self._position.x, self._position.y))

        r_pixels = ((mouse_x_pixels - body_x_pixels)**2 + (mouse_y_pixels - body_y_pixels)**2)**(1/2)

        return r_pixels < MARKER_SENSITIVITY

    def _pixels_to_distance(self, pixels: int) -> float:
        """Converts a pixel size to a axes distance size."""
        x1, _ = self._axis.transData.inverted().transform((0, 0))
        x2, _ = self._axis.transData.inverted().transform((pixels, 0))
        return x2 - x1
