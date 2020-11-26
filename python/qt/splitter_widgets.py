# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QPaintEvent
from PyQt5.QtWidgets import QSplitter, QSplitterHandle


class SplitterHandle(QSplitterHandle):
    """A class used to create a QSplitterHandle with a QIcon."""

    def __init__(self, parent: QSplitter, icon: QIcon, orientation: Qt.Orientation):
        """Initialize the splitter handle with an icon."""
        super(SplitterHandle, self).__init__(orientation, parent)
        self.icon = icon

    def paintEvent(self, event: QPaintEvent) -> None:
        """Override the paint event method to paint an icon onto the splitter handle."""
        super().paintEvent(event)
        self.icon.paint(QPainter(self), int(self.size().width() / 2), -9, 24, 24)


class Splitter(QSplitter):
    """A class used to create a QSplitter with a QIcon."""

    def __init__(self, icon: QIcon):
        """Initialize the splitter with an icon."""
        super(Splitter, self).__init__(None)
        self.icon = icon

    def createHandle(self) -> QSplitterHandle:
        """Override the create handle method to use the custom splitter handle."""
        return SplitterHandle(self, self.icon, Qt.Vertical)
