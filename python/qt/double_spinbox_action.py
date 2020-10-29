# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from PyQt5.QtWidgets import QDoubleSpinBox, QHBoxLayout, QLabel, QWidget, QWidgetAction


class DoubleSpinBoxAction(QWidgetAction):
    """A class which creates a custom QMenu action made up of a QLabel and QDoubleSpinBox."""

    def __init__(self, label: str, default_value: float, minimum: float, maximum: float, suffix: str):
        """Initializes the QLabel, QDoubleSpinBox, and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.double_spin_box = QDoubleSpinBox(None)
        self.double_spin_box.setMinimum(minimum)
        self.double_spin_box.setMaximum(maximum)
        self.double_spin_box.setValue(default_value)
        self.double_spin_box.setSuffix(suffix)

        self.layout = QHBoxLayout()
        self.layout.addWidget(QLabel(label))
        self.layout.addWidget(self.double_spin_box)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)
