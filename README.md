# N-Body Simulator
![windows workflow](https://img.shields.io/github/workflow/status/robertapplin/N-Body-Simulations/Windows?label=Windows%20latest)
![ubuntu workflow](https://img.shields.io/github/workflow/status/robertapplin/N-Body-Simulations/Ubuntu?label=Ubuntu%20latest)
![test coverage](https://img.shields.io/badge/Test%20Coverage-High-brightgreen)

This project creates a QWidget used for simulating a gravitational system of N bodies in two dimensions. These bodies will merge together if they get close enough to each other. 

## Table of contents
* [About](#about)
* [Features](#features)
* [Screengrab](#Screengrab)
* [Setup](#setup)

## About

The purpose of this project was to develop my programming skills by creating a maintainable and well-tested cross-platform application. In this project I have created a simulator for N-Body gravitational systems which allows the collision and merging of bodies. The **docs** folder contains example \**.txt* files which can be loaded into this widget.

The following units have been used for this project:

  |Quantity  |Measured in               |Unit|
  |----------|--------------------------|----|
  |Mass      |Solar masses              |M*  |
  |Position  |Astronomical units        |au  |
  |Time      |Days                      |d   |
  |Velocity  |Astronomical units per day|au/d|

## Features

The widget has several options which are found above the data table:

  |Button                                                                            |Description                                                                    |
  |----------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
  |<img align="centre" width="25" height="25" src="docs/load_button.PNG">            |Load a \**.txt* file containing initial parameters for an N-Body-Simulation.   |
  |<img align="centre" width="25" height="25" src="docs/save_button.PNG">            |Save the initial parameters of an N-Body-Simulation to a \**.txt* file.        |
  |<img align="centre" width="25" height="25" src="docs/remove_button.PNG">          |Remove the selected bodies from the simulation.                                |
  |<img align="centre" width="25" height="25" src="docs/add_button.PNG">             |Add bodies to the simulation.                                                  |
  |<img align="centre" width="25" height="25" src="docs/time_options_button.PNG">    |Adjust the time step and duration of the simulation.                           |
  |<img align="centre" width="25" height="25" src="docs/plotting_options_button.PNG">|Show or hide position labels and velocity arrows on the plot.                  |
  |<img align="centre" width="25" height="25" src="docs/interactive_mode_button.PNG">|Turn on interactive mode, allowing you to interact with the bodies on the plot.|
  |<img align="centre" width="25" height="25" src="docs/stop_button.PNG">            |Stop the simulation.                                                           |
  |<img align="centre" width="25" height="25" src="docs/play_pause_button.PNG">      |Play or Pause the simulation.                                                  |

The widget also includes an interactive plot where you can:

  |Image                                                                 |Description                                                                          |
  |----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
  |<img align="left" width="83" height="25" src="docs/body.PNG">         |Adjust the colour and name used to represent a body.                                 |
  |<img align="left" width="83" height="25" src="docs/body_position.PNG">|Adjust the position of a body by dragging the body on the interactive plot.          |
  |<img align="left" width="83" height="25" src="docs/body_velocity.PNG">|Adjust the velocity of a body by dragging the velocity arrow on the interactive plot.|

## Screengrab

<p align="center">
  <img src="docs/three-body-simulation.gif" alt="animated">
</p>

## Setup

Follow the instructions for the appropriate operating system:

```diff
+ Windows
! Ubuntu
```

This widget was created using **Python v3.8**, and using **CMake v3.12**. These versions are a minimum requirement. It is also recommended that you download and install the python package manager [Miniconda3](https://docs.conda.io/en/latest/miniconda.html).

The first step is to clone the code in this repository using [git](https://git-scm.com/downloads).

```sh
git clone git@github.com:robertapplin/N-Body-Simulations.git
```

The dependencies for this project can be installed using Miniconda:

```sh
conda install -c anaconda pytest-mock pyqt qtawesome
conda install -c conda-forge matplotlib pybind11 pyside2 pytest pytest-qt
```

Create a build folder from the project root directory and enter this folder.

```sh
mkdir build
cd build
```

Generate the build files. Follow the colour corresponding to your operating system:

```diff
+ cmake .. -DPYTHON_LIBRARY_DIR=<path>/Miniconda/lib/site-packages/ -DPYTHON_EXECUTABLE=<path>/Miniconda/python.exe
! cmake .. -DPYTHON_LIBRARY_DIR=<path>/miniconda3/lib/python3.8/site-packages/ -DPYTHON_EXECUTABLE=<path>/miniconda3/bin/python
```

Then build the project in Release mode:

```sh
cmake --build . --config Release
```

Finally you can install the project into the Miniconda site-packages folder:

```
cmake --install .
```

Run the **startup.py** script from your chosen python environment to open this QWidget.
