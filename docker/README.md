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
winpty docker run --rm -u=root -it n-body-simulations:latest \
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

### Pulling from Dockerhub

There is also the option to pull the image from [Dockerhub](https://hub.docker.com/r/robertapplin/n-body-simulations).

```sh
docker pull robertapplin/n-body-simulations
```

You would then need to change the tag on the image so that it can be picked up by the ``docker-compose.yml`` file.

```sh
docker tag robertapplin/n-body-simulations n-body-simulations
```
