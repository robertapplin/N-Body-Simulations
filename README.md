## About

This project creates a QWidget used for simulating a gravitational system of N bodies in two dimensions. The widget has options to:

* Save and load the initial parameters for an N-body simulation.
* Add and remove bodies from the simulation.
* Adjust the time step and duration of the simulation.
* Show or hide position labels and velocity arrows.
* Play, Pause or Stop the simulation at will.

The widget also includes an interactive plot where you can:

* Adjust the colour and name used to represent a body.
* Adjust the position of a body by dragging the body on the interactive plot.
* Adjust the velocity of a body by dragging the velocity arrow on the interactive plot.
* Bodies will merge together if they get close enough to each other.

<p align="center">
  <img src="docs/three-body-simulation.gif" alt="animated">
</p>

The **docs** folder has example \**.txt* files which can be loaded into the widget.

## Units

Mass - Solar masses (M*)
Position - Astronomical units (au)
Time - Days (d)
Velocity - (au/d)

## Building On Windows

The easiest way to build this project is to download and install Miniconda. The dependencies for this project can then be installed:

```sh
conda install -c anaconda pytest-mock pyqt qtawesome
conda install -c conda-forge matplotlib pybind11 pyside2 pytest
```

The code for this project should then be cloned:

```sh
git clone git@github.com:robertapplin/N-Body-Simulations.git
```

CMake was used to create this widget. Using the command prompt you should create a build folder, and then cmake the project:

```sh
mkdir build
cd build
cmake .. -DPYTHON_LIBRARY_DIR=<path>/Miniconda/lib/site-packages/ -DPYTHON_EXECUTABLE=<path>/Miniconda/python.exe
cmake --build . --config Release
```

It might be necessary to specify a compiler when running **cmake**:

```sh
cmake .. -DPYTHON_LIBRARY_DIR=<path>/Miniconda/lib/site-packages/ -DPYTHON_EXECUTABLE=<path>/Miniconda/python.exe -G "Visual Studio 15 2017 Win64"
```

Run the **startup.py** script from your chosen python environment to open this QWidget.
