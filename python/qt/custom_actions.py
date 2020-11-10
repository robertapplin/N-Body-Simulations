# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml_reader import get_user_interface_property

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QWidget,
                             QWidgetAction)


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
        self.double_spin_box.setSingleStep(float(get_user_interface_property(item_type + "-step")))
        self.double_spin_box.setValue(float(get_user_interface_property(item_type + "-default")))
        self.double_spin_box.setSuffix(" " + get_user_interface_property("time-unit"))

        self.layout = QHBoxLayout()
        self.layout.addWidget(QLabel(label))
        self.layout.addWidget(self.double_spin_box)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)


class LineEditButtonAction(QWidgetAction):
    """A class which creates a custom QMenu action made up of a QLineEdit and QPushbutton."""

    def __init__(self, button: str, regex: str):
        """Initializes the QLineEdit, QPushbutton, and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.line_edit = QLineEdit()
        self.line_edit.setValidator(QRegExpValidator(QRegExp(regex)))

        self.push_button = QPushButton(button)
        self.push_button.setFixedSize(100, 23)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.push_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)


class SpinBoxButtonAction(QWidgetAction):
    """A class which creates a custom QMenu action made up of a QSpinBox and QPushbutton."""

    def __init__(self, button: str, minimum: int = 1, maximum: int = 20):
        """Initializes the QSpinBox, QPushbutton, and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(minimum)
        self.spin_box.setMaximum(maximum)

        self.push_button = QPushButton(button)
        self.push_button.setFixedSize(100, 23)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.spin_box)
        self.layout.addWidget(self.push_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)
