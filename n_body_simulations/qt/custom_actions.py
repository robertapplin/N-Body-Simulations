# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.xml.xml_reader import get_simulation_setting, get_user_interface_property

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (QDoubleSpinBox, QComboBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSlider, QSpinBox,
                             QWidget, QWidgetAction)


class AnimationFrameDelayAction(QWidgetAction):
    """A class which creates a custom action used for adjusting the speed of the animation."""

    def __init__(self):
        """Initializes the QSlider and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.delay_slider = QSlider(Qt.Horizontal)
        self.delay_slider.setValue(int(get_user_interface_property("frame-delay-default")))
        self.delay_slider.setToolTip(f"Animation frame delay in milliseconds. "
                                     f"Current delay is {self.delay_slider.value()} ms.")

        self.delay_label = QLabel()
        self.delay_label.setText(f"{self.delay_slider.value()} ms")
        self.delay_label.setMinimumWidth(42)
        self.delay_label.setMaximumWidth(42)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.delay_slider)
        self.layout.addWidget(self.delay_label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)


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
        self.double_spin_box.setDecimals(int(get_user_interface_property("time-dp")))
        self.double_spin_box.setSingleStep(float(get_user_interface_property(item_type + "-step")))
        self.double_spin_box.setValue(float(get_simulation_setting(item_type + "-default")))
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


class PositionPlotOptionsAction(QWidgetAction):
    """A class which creates a custom action used for position plotting options."""

    def __init__(self):
        """Initializes the QPushbutton and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.show_labels_button = QPushButton("Hide Position Labels")
        self.show_labels_button.setFixedSize(150, 23)

        self.label_spacer = QLabel()
        self.label_spacer.setMinimumWidth(42)
        self.label_spacer.setMaximumWidth(42)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.show_labels_button)
        self.layout.addWidget(self.label_spacer)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)

    def set_is_showing_labels(self, is_showing_labels: bool) -> None:
        """Set the text shown on the button."""
        self.show_labels_button.setText("Hide Position Labels" if is_showing_labels else "Show Position Labels")

    def showing_position_labels(self) -> bool:
        """Checks if the position labels are being shown."""
        return self.show_labels_button.text() == "Show Position Labels"


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


class VelocityPlotOptionsAction(QWidgetAction):
    """A class which creates a custom action used for velocity plotting options."""

    def __init__(self):
        """Initializes the QPushbutton and layout of this custom action."""
        super(QWidgetAction, self).__init__(None)

        self.show_arrows_button = QPushButton("Hide Velocity Arrows")
        self.show_arrows_button.setFixedSize(150, 23)

        self.arrow_magnification = QComboBox()
        self.arrow_magnification.setMinimumWidth(42)
        self.arrow_magnification.setMaximumWidth(42)
        self.arrow_magnification.addItems(["x1", "x2", "x4", "x8", "x16", "x32", "x64"])
        self.arrow_magnification.setToolTip("The factor to magnify the velocity arrows by.")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.show_arrows_button)
        self.layout.addWidget(self.arrow_magnification)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setDefaultWidget(self.widget)

    def set_is_showing_arrows(self, is_showing_arrows: bool) -> None:
        """Set the text shown on the button."""
        self.show_arrows_button.setText("Hide Velocity Arrows" if is_showing_arrows else "Show Velocity Arrows")

    def showing_velocity_arrows(self) -> bool:
        """Checks if the velocity arrows are being shown."""
        return self.show_arrows_button.text() == "Show Velocity Arrows"
