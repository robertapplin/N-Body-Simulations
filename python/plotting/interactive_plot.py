# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from simulation_animator import SimulationAnimator

from matplotlib.animation import FuncAnimation
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
        self._animation = None
        self._simulation_data = None
        self._pause = False

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

    def set_simulation_data(self, body_positions: dict) -> None:
        self._simulation_data = body_positions

    def time_step(self):
        times = list(list(self._simulation_data.values())[0].keys())
        return abs(times[-1] / (len(times) - 1))

    def duration(self):
        return list(list(self._simulation_data.values())[0].keys())[-1]

    def stop(self):
        if self._animation is not None:
            self._animation.event_source.stop()

    def pause(self):
        self._pause = True

    def play(self):
        self._pause = False

    def time(self):
        t = 0.0
        t_max = self.duration()
        time_step = self.time_step()
        while t < t_max:
            if not self._pause:
                t += time_step
            yield t

    def animate_bodies(self, time: float) -> dict:
        for body_name, positions in self._simulation_data.items():
            self._lines[body_name].set_xdata(positions[time].x)
            self._lines[body_name].set_ydata(positions[time].y)
        return self._lines

    def animate(self):
        self._animation = FuncAnimation(self._figure, self.animate_bodies, self.time, interval=3)
        self.show_legend()
        self.draw()

    # Temporarily in place of a simulation
    def plot_trail(self, body_name: str, positions: list) -> None:
        xs, ys = [], []
        for position in positions.values():
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

    def update_axes_limits(self) -> None:
        x_min, x_max, y_min, y_max = self._calculate_axes_min_max()

        x_margin = (x_max-x_min)*AXIS_MARGIN
        y_margin = (y_max-y_min)*AXIS_MARGIN

        self._ax.set_xlim(x_min - x_margin, x_max + x_margin)
        self._ax.set_ylim(y_min - y_margin, y_max + y_margin)

    def _calculate_axes_min_max(self) -> tuple:
        xs, ys = [], []
        for body_positions in self._simulation_data.values():
            for position in body_positions.values():
                xs.append(position.x)
                ys.append(position.y)
        return min(xs), max(xs), min(ys), max(ys)
