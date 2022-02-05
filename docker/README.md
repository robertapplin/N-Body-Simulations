## Docker Container

This document provides a guide for building the ``Dockerfile`` in this repository, and then running the N-Body Simulations widget within a container from Windows. You will need to install [Xming X Server for Windows](https://sourceforge.net/projects/xming/) before continuing with this guide, as well as [Docker Desktop](https://docs.docker.com/desktop/windows/install/). You might also need to ``pip install winpty``.

Firstly, make sure you have your command prompt open in the ``docker`` directory:

```sh
cd docker/
```

Start the Docker Daemon, and start an Xming X Server with the default settings. There is now two avenues for building the image and running a container as explained below. 

### Using the Dockerfile

Build the ``Dockerfile`` with tag ``n-body-simulations``:

```sh
docker build --no-cache -t n-body-simulations .
```

Then run the image and mount the config files into the container:

```sh
winpty docker run -u=root -it -e DISPLAY=host.docker.internal:0.0 -e LIBGL_ALWAYS_INDIRECT=1 -e XDG_RUNTIME_DIR=/tmp/runtime-root \
--mount "type=bind,source=$PWD/config/lightdm.conf,target=/etc/lightdm/lightdm.conf.d/lightdm.conf" \
--mount "type=bind,source=$PWD/config/default-display-manager,target=/etc/X11/default-display-manager" \
n-body-simulations:latest \
bash -c ". /opt/env/bin/activate && python3 /usr/N-Body-Simulations/n_body_simulations/startup.py"
```

The N-Body Simulations widget should open within a containerized Ubuntu environment.

### Using Docker Compose

Build the ``n-body-simulations`` service seen in the ``docker-compose.yml`` file:

```sh
docker-compose build n-body-simulations
```

Then simply run the container with the configuration seen in the ``docker-compose.yml`` file:

```sh
docker-compose run --rm n-body-simulations
```

The N-Body Simulations widget should open within a containerized Ubuntu environment.
