# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020


class SignalBlocker:
    """A class for blocking the signals of widgets."""

    def __init__(self, *widgets):
        """Initializes the signal blocker by blocking the signals of the widgets."""
        self._widgets = widgets
        self._block_signals(True)

    def __del__(self):
        """Unblocks the widget signals upon going out-of-scope."""
        self._block_signals(False)

    def _block_signals(self, block: bool) -> None:
        """Blocks or unblocks the signals of the stored widgets."""
        for widget in self._widgets:
            widget.blockSignals(block)
