## N-Body Simulator
![windows workflow](https://img.shields.io/github/workflow/status/robertapplin/N-Body-Simulations/Windows?label=Windows%20latest)
![ubuntu workflow](https://img.shields.io/github/workflow/status/robertapplin/N-Body-Simulations/Ubuntu?label=Ubuntu%20latest)
![test coverage](https://img.shields.io/badge/Test%20Coverage-High-brightgreen)

This project creates a QWidget used for simulating a gravitational system of N bodies in two dimensions. These bodies will merge together if they get close enough to each other. The widget has options to:

* Load a \**.txt* file containing initial parameters for an N-Body-Simulation. <img align="left" width="25" height="25" src="docs/load_button.PNG">
* Save the initial parameters of an N-Body-Simulation to a \**.txt* file. <img align="left" width="25" height="25" src="docs/save_button.PNG">
* Remove the selected bodies from the simulation. <img align="left" width="25" height="25" src="docs/remove_button.PNG">
* Add bodies to the simulation. <img align="left" width="25" height="25" src="docs/add_button.PNG">
* Adjust the time step and duration of the simulation. <img align="left" width="25" height="25" src="docs/time_options_button.PNG">
* Show or hide position labels and velocity arrows on the plot. <img align="left" width="25" height="25" src="docs/plotting_options_button.PNG">
* Turn on interactive mode, allowing you to interact with the bodies on the plot. <img align="left" width="25" height="25" src="docs/interactive_mode_button.PNG">
* Stop the simulation. <img align="left" width="25" height="25" src="docs/stop_button.PNG">
* Play or Pause the simulation. <img align="left" width="25" height="25" src="docs/play_pause_button.PNG">

The widget also includes an interactive plot where you can:

* Adjust the colour and name used to represent a body. <img align="left" width="83" height="25" src="docs/body.PNG">
* Adjust the position of a body by dragging the body on the interactive plot. <img align="left" width="83" height="25" src="docs/body_position.PNG">
* Adjust the velocity of a body by dragging the velocity arrow on the interactive plot. <img align="left" width="83" height="25" src="docs/body_velocity.PNG">

<p align="center">
  <img src="docs/three-body-simulation.gif" alt="animated">
</p>

The **docs** folder has example \**.txt* files which can be loaded into the widget.

## Units

  |Quantity  |Measured in               |Unit|
  |----------|--------------------------|----|
  |Mass      |Solar masses              |M*  |
  |Position  |Astronomical units        |au  |
  |Time      |Days                      |d   |
  |Velocity  |Astronomical units per day|au/d|

## Building the N-Body Simulator

This widget was created using Python v3.8, and using CMake v3.12. These versions are a minimum requirement.

The easiest way to build this project is to download and install Miniconda3. The dependencies for this project can be installed from the **command line** or **terminal**:

```sh
conda install -c anaconda pytest-mock pyqt qtawesome
conda install -c conda-forge matplotlib pybind11 pyside2 pytest pytest-qt
```

Clone the code in this repository using **git**:

```sh
git clone git@github.com:robertapplin/N-Body-Simulations.git
```

### Windows

Using the **command line** create a build folder from the project root directory, and then cmake the project:

```sh
mkdir build
cd build
cmake .. -DPYTHON_LIBRARY_DIR=<path>/Miniconda/lib/site-packages/ -DPYTHON_EXECUTABLE=<path>/Miniconda/python.exe
cmake --build . --config Release
```

It might be necessary to specify a compiler when running **cmake** using the **-G** flag:

```sh
cmake .. -DPYTHON_LIBRARY_DIR=... -DPYTHON_EXECUTABLE=... -G "Visual Studio 15 2017 Win64"
```

Next, make sure to install the project into the Miniconda site-packages folder:

```
cmake --install .
```

Run the **startup.py** script from your chosen python environment to open this QWidget.

### Ubuntu

Using the **terminal** create a build folder from the project root directory, and then cmake the project:

```sh
mkdir build
cd build
cmake .. -DPYTHON_LIBRARY_DIR=<path>/miniconda3/lib/python3.8/site-packages/ -DPYTHON_EXECUTABLE=<path>/miniconda3/bin/python
cmake --build . --config Release
```

The g++ compiler was used when running **cmake**. It can be installed from the **terminal**:

```sh
sudo apt-get install g++
```

If you are using an earlier version of CMake than v3.12, an up-to-date version can be installed from the **terminal**:

```sh
sudo apt remove --purge cmake
sudo snap install cmake --classic
```

Next, make sure to install the project into the Miniconda site-packages folder:

```
cmake --install .
```

Run the **startup.py** script from your chosen python environment to open this QWidget.
