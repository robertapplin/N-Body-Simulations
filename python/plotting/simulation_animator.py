# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

MARKER = '.'


class SimulationAnimator:

    def __init__(self):
        self._lines = dict()

        self._animation = None
        self._simulation_data = None
        self._pause = False

    def set_simulation_data(self, simulation_data: dict) -> None:
        self._simulation_data = simulation_data

    def simulation_data(self) -> dict:
        return self._simulation_data

    def stop(self) -> None:
        if self._animation is not None:
            self._animation.event_source.stop()

    def pause(self) -> None:
        self._pause = True

    def play(self) -> None:
        self._pause = False

    def start(self, figure: FigureCanvas, lines: dict) -> None:
        self._lines = lines
        self._animation = FuncAnimation(figure, self._update_body_positions, self._time, interval=3)

    def _update_body_positions(self, time: float) -> dict:
        for body_name, positions in self._simulation_data.items():
            self._lines[body_name].set_xdata(positions[time].x)
            self._lines[body_name].set_ydata(positions[time].y)
        return self._lines

    def _time(self) -> float:
        t, t_max = 0.0, self._duration()
        time_step = self._time_step()

        while t < t_max:
            if not self._pause:
                t += time_step
            yield t

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
