[![Coverage Status](https://coveralls.io/repos/robertapplin/N-Body-Simulations/badge.svg?branch=master)](https://coveralls.io/r/robertapplin/N-Body-Simulations?branch=master)

## About The Project

This project creates a QWidget used for simulating and animating a system of N bodies. A detailed explanation for how to use this widget can be found in the `docs` folder. The widget can:

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

```sh
cmake .. -DPYTHON_LIBRARY_DIR="C:/Users/rober/miniconda3/Lib/site-packages" -DPYTHON_EXECUTABLE="C:/Users/rober/miniconda3/python.exe" -G "Visual Studio 15 2017 Win64"
```

## Building On Linux
