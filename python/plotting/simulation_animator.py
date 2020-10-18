# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from qt.error_catcher import catch_errors

MARKER = '.'


class SimulationAnimator:

    def __init__(self, figure: FigureCanvas):
        self._lines = dict()

        self._figure = figure

        self._animation = None
        self._simulation_data = None
        self._playing = False
        self._active = False
        self._t = 0.0

    def disable(self) -> None:
        self._active = False
        self.stop()
        if self._animation:
            self._animation.event_source.stop()

    def enable(self, lines: dict) -> None:
        if self._active:
            self.disable()

        self._active = True
        self._lines = lines
        self._animation = FuncAnimation(self._figure, self._update_body_positions, self._time, interval=3)

    def is_enabled(self) -> bool:
        return self._active

    def set_simulation_data(self, simulation_data: dict) -> None:
        self._simulation_data = simulation_data

    def simulation_data(self) -> dict:
        return self._simulation_data

    def stop(self) -> None:
        self._playing = False
        self._t = 0.0

    def pause(self) -> None:
        self._playing = False

    def play(self) -> None:
        self._playing = True

    def start(self, lines: dict) -> None:
        self.enable(lines)
        self.play()

    def _update_body_positions(self, time: float) -> dict:
        for body_name, positions in self._simulation_data.items():
            self._lines[body_name].set_xdata(positions[time].x)
            self._lines[body_name].set_ydata(positions[time].y)
        return self._lines

    def _time(self) -> float:
        self._t = 0.0
        t_max = self._duration()
        time_step = self._time_step()

        while self._t < t_max:
            if self._playing:
                self._t += time_step
            yield self._t

    def _time_step(self):
        times = list(list(self._simulation_data.values())[0].keys())
        return abs(times[-1] / (len(times) - 1))

    def _duration(self):
        return list(list(self._simulation_data.values())[0].keys())[-1]

    # Temporarily here for debugging
    def _plot_trail(self, body_name: str, positions: list) -> None:
        xs, ys = [], []
        for position in positions.values():
            xs.append(position.x)
            ys.append(position.y)

        if body_name in self._lines.keys():
            self.remove_body(body_name)

        lines = self._ax.plot(xs, ys, marker=MARKER, label=body_name)
        self._lines[body_name] = lines[0]