[![Coverage Status](https://coveralls.io/repos/robertapplin/N-Body-Simulations/badge.svg?branch=master)](https://coveralls.io/r/robertapplin/N-Body-Simulations?branch=master)

## About The Project

![](docs/three-body-simulation.gif)

In this project I have created a QWidget used for simulating and animating a system of N bodies. This widget allows you to add a large number of bodies with different masses, positions, and velocities before performing a simulation for a given time step and duration. The results from the simulation are then animated using matplotlib. Prior to a simulation, the position and velocity of a body can be interactively dragged on the matplotlib plot. A more detailed explanation for how to use this widget can be found in the 'docs' folder.

## Building On Windows

```
cmake .. -DPYTHON_LIBRARY_DIR="C:/Users/rober/miniconda3/Lib/site-packages" -DPYTHON_EXECUTABLE="C:/Users/rober/miniconda3/python.exe" -G "Visual Studio 15 2017 Win64"
```

## Building On Linux
