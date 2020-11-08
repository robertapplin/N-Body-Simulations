# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from NBodySimulations import Vector2D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.patches import Circle, Patch

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QCursor

BODY_RADIUS = 3  # In pixels
MARKER_SENSITIVITY = 5


class BodyMarker(QObject):
    bodyMovedSignal = pyqtSignal(str, float, float)

    def __init__(self, canvas: FigureCanvas, name: str, position: Vector2D, colour: str):
        super(BodyMarker, self).__init__()

        self._canvas = canvas
        self._axis = self._canvas.figure.get_axes()[0]

        self.name = name
        self.position = tuple([position.x, position.y])
        self.colour = colour

        self._override_cursor = None
        self._is_dragging = False

        self._create_body()

    def mouse_drag_start(self, x: float, y: float) -> bool:
        self._is_dragging = self._is_above(x, y)
        if self._is_dragging:
            self._set_override_cursor(x, y)
            return True
        return False

    def mouse_drag_stop(self, x: float, y: float) -> bool:
        if self._is_dragging:
            self.set_position(x, y)
            self._is_dragging = False
            self._set_override_cursor(x, y)
            return True
        return False

    def mouse_moved(self, x: float, y: float) -> bool:
        self._set_override_cursor(x, y)
        if self._is_dragging:
            self.set_position(x, y)
            return True
        return False

    def remove_body(self) -> None:
        self._patch.remove()

    def set_position(self, x: float, y: float, emit_signal: bool = True) -> None:
        self.remove_body()
        self.position = tuple([x, y])
        self._create_body()

        if emit_signal:
            self.bodyMovedSignal.emit(self.name, x, y)

    def get_patch(self) -> Patch:
        return self._patch

    def get_override_cursor(self) -> QCursor:
        return self._override_cursor

    def _set_override_cursor(self, x: float, y: float) -> None:
        if self._is_dragging:
            self._override_cursor = Qt.ClosedHandCursor
        elif not self._is_dragging and self._is_above(x, y):
            self._override_cursor = Qt.OpenHandCursor
        else:
            self._override_cursor = None

    def _create_body(self) -> None:
        self._patch = Circle(self.position, self._body_radius(), facecolor=self.colour)
        self._axis.add_patch(self._patch)

    def _is_above(self, x: float, y: float) -> bool:
        mouse_x_pixels, mouse_y_pixels = self._axis.transData.transform((x, y))
        body_x_pixels, body_y_pixels = self._axis.transData.transform(self.position)

        r_pixels = ((mouse_x_pixels - body_x_pixels)**2 + (mouse_y_pixels-body_y_pixels)**2)**(1/2)

        return r_pixels < MARKER_SENSITIVITY

    def _body_radius(self) -> float:
        x1, _ = self._axis.transData.inverted().transform((0, 0))
        x2, _ = self._axis.transData.inverted().transform((BODY_RADIUS, 0))
        return x2 - x1
