# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from plotting.simulation_animator import SimulationAnimator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

AXIS_MARGIN = 0.05  # 5% axis margin
LINESTYLE = " "
MARKER = '.'


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

        self._animator = SimulationAnimator()

    def canvas(self) -> FigureCanvas:
        return self._canvas

    def clear(self) -> None:
        self._ax.clear()

    def draw_body(self, body_name: str, x: int, y: int) -> None:
        lines = self._ax.plot(x, y, label=body_name, marker=MARKER, linestyle=LINESTYLE)
        self._lines[body_name] = lines[0]
        self.draw()

    def remove_body(self, body_name: str) -> None:
        self._lines[body_name].remove()
        del self._lines[body_name]
        self.draw()

    def set_simulation_data(self, simulation_data: dict) -> None:
        self._animator.set_simulation_data(simulation_data)

    def stop_animation(self) -> None:
        self._animator.stop()

    def pause_animation(self) -> None:
        self._animator.pause()

    def play_animation(self) -> None:
        self._animator.play()

    def start_animation(self):
        self._animator.start(self._figure, self._lines)
        self.show_legend()
        self.draw()

    def show_legend(self) -> None:
        self._ax.legend()

    def draw(self) -> None:
        self._canvas.draw()

    def update_axes_limits(self) -> None:
        x_min, x_max, y_min, y_max = self._calculate_axes_min_max()

        x_margin = (x_max-x_min)*AXIS_MARGIN
        y_margin = (y_max-y_min)*AXIS_MARGIN

        self._ax.set_xlim(x_min - x_margin, x_max + x_margin)
        self._ax.set_ylim(y_min - y_margin, y_max + y_margin)

    def _calculate_axes_min_max(self) -> tuple:
        xs, ys = [], []
        for body_positions in self._animator.simulation_data().values():
            for position in body_positions.values():
                xs.append(position.x)
                ys.append(position.y)
        return min(xs), max(xs), min(ys), max(ys)
