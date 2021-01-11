## About

This project creates a QWidget used for simulating a gravitational system of N bodies. A detailed explanation for how to use this widget can be found in the `docs` folder. The widget can:

* Add and remove bodies from the simulation.
* Adjust the position of a body by dragging the body on the interactive plot.
* Adjust the velocity of a body by dragging the velocity arrow on the interactive plot.
* Change the time step and duration of the simulation.
* Change the colour and name used to represent a body.
* Save and load the initial parameters for an N-body simulation.

If two bodies get close enough to each other, they will merge into one body.

<p align="center">
  <img src="docs/three-body-simulation.gif" alt="animated">
</p>

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

It might be necessary to specify a compiler when running `cmake`:

```sh
cmake .. -DPYTHON_LIBRARY_DIR=<path>/Miniconda/lib/site-packages/ -DPYTHON_EXECUTABLE=<path>/Miniconda/python.exe -G "Visual Studio 15 2017 Win64"
```

Run the `startup.py` script from your chosen python environment to open this QWidget.
