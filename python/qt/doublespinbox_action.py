# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QDoubleSpinBox, QWidget, QWidgetAction


class DoubleSpinBoxAction(QWidgetAction):
    """A class which creates a custom QMenu action made up of a QLabel and QDoubleSpinBox."""

    def __init__(self, label: str, default_value: float, minimum: float, maximum: float, suffix: str):
        """Initializes the QLabel, QDoubleSpinBox, and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.doubleSpinBox = QDoubleSpinBox(None)
        self.doubleSpinBox.setMinimum(minimum)
        self.doubleSpinBox.setMaximum(maximum)
        self.doubleSpinBox.setValue(default_value)
        self.doubleSpinBox.setSuffix(suffix)

        self.layout = QHBoxLayout()
        self.layout.addWidget(QLabel(label))
        self.layout.addWidget(self.doubleSpinBox)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)
