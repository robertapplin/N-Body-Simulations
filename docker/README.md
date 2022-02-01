## Docker Container

This document provides a guide for building the ``Dockerfile`` in this repository, and then running the N-Body Simulations widget within a container from Windows. You will need to install [Xming X Server for Windows](https://sourceforge.net/projects/xming/) before continuing with this guide, as well as [Docker Desktop](https://docs.docker.com/desktop/windows/install/). You might also need to ``pip install winpty``.

Firstly, make sure you have your command prompt open in the ``docker`` directory:

```sh
cd docker/
```

Start the Docker Daemon, and then build the ``Dockerfile`` with tag ``n-body-simulations``:

```sh
docker build --no-cache -t n-body-simulations .
```

After the build has finished, start Xming X Server with the default settings. Run the image and mount the config files into the container:

```sh
winpty docker run -u=root -it --mount "type=bind,source=$PWD/config/lightdm.conf,target=/etc/lightdm/lightdm.conf.d/lightdm.conf" --mount "type=bind,source=$PWD/config/default-display-manager,target=/etc/X11/default-display-manager" n-body-simulations:latest
```

The N-Body Simulations widget should open within an containerized Ubuntu environment.
