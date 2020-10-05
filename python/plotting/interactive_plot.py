# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

MARKER = '.'
from qt.error_catcher import catch_errors


class InteractivePlot:

    def __init__(self):
        self._figure = Figure()
        # Modify margins around a figure
        self._figure.subplots_adjust(left=0.2, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)
        self._figure.patch.set_facecolor('#f0f0f0')
        self._ax = self._figure.add_subplot(111)
        self._ax.set_autoscale_on(True)
        self._canvas = FigureCanvas(self._figure)

        self._lines = dict()

    def canvas(self) -> FigureCanvas:
        return self._canvas

    def clear(self) -> None:
        self._ax.clear()

    def draw_body(self, body_name: str, x: int, y: int) -> None:
        lines = self._ax.plot(x, y, marker=MARKER, label=body_name)
        self._lines[body_name] = lines[0]
        self.draw()

    def remove_body(self, body_name: str) -> None:
        self._lines[body_name].remove()
        del self._lines[body_name]
        self.draw()

    def plot_trail(self, body_name: str, positions: list) -> None:
        xs, ys = [], []
        for position in positions:
            xs.append(position.x)
            ys.append(position.y)

        if body_name in self._lines.keys():
            self.remove_body(body_name)

        lines = self._ax.plot(xs, ys, marker=MARKER, label=body_name)
        self._lines[body_name] = lines[0]

    def show_legend(self) -> None:
        self._ax.legend()

    def draw(self) -> None:
        self._canvas.draw()

    def update_axes_limits(self):
        xs, ys = [], []
        for line in self._lines.values():
            xs.extend(list(line.get_xdata()))
            ys.extend(list(line.get_ydata()))

        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)
        x_space = (x_max-x_min)*0.05
        y_space = (y_max-y_min)*0.05

        self._ax.set_xlim(x_min - x_space, x_max + x_space)
        self._ax.set_ylim(y_min - y_space, y_max + y_space)
