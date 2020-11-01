# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml_reader import get_user_interface_property

from PyQt5.QtWidgets import QDoubleSpinBox, QHBoxLayout, QLabel, QWidget, QWidgetAction


class DoubleSpinBoxAction(QWidgetAction):
    """A class which creates a custom QMenu action made up of a QLabel and QDoubleSpinBox."""

    TimeStep = "time-step"
    Duration = "duration"

    def __init__(self, label: str, item_type: str):
        """Initializes the QLabel, QDoubleSpinBox, and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.double_spin_box = QDoubleSpinBox(None)
        self.double_spin_box.setMinimum(float(get_user_interface_property(item_type + "-min")))
        self.double_spin_box.setMaximum(float(get_user_interface_property(item_type + "-max")))
        self.double_spin_box.setValue(float(get_user_interface_property(item_type + "-default")))
        self.double_spin_box.setSuffix(" " + get_user_interface_property("time-unit"))

        self.layout = QHBoxLayout()
        self.layout.addWidget(QLabel(label))
        self.layout.addWidget(self.double_spin_box)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)
