# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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
        lines = self._ax.plot(x, y, '*-')
        self._lines[body_name] = lines[0]
        self._canvas.draw()

    def remove_body(self, body_name: str) -> None:
        self._lines[body_name].remove()
        del self._lines[body_name]
        self._canvas.draw()
