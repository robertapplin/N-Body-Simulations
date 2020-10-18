# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

ANIMATION_INTERVAL = 3
MARKER = '.'


class SimulationAnimator:

    def __init__(self, figure: FigureCanvas):
        self._figure = figure
        self._animation = None

        self._lines = dict()
        self._simulation_data = dict()
        self._t = 0.0

        self._playing = False
        self._active = False

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
        self._animation = FuncAnimation(self._figure, self._update_body_positions, self._time,
                                        interval=ANIMATION_INTERVAL)

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

    def _time_step(self) -> float:
        times = list(list(self._simulation_data.values())[0].keys())
        return abs(times[-1] / (len(times) - 1))

    def _duration(self) -> float:
        return list(list(self._simulation_data.values())[0].keys())[-1]
