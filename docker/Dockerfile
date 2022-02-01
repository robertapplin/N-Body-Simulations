#####
## Docker image for N-Body-Simulations
#####

# Install the Ubuntu latest base image
FROM ubuntu:latest

# To avoid user interaction during the installation of cmake
ARG DEBIAN_FRONTEND=noninteractive

# Create git repository variable
ARG GIT_REPOSITORY=https://github.com/robertapplin/N-Body-Simulations

# Install packages required in the container environment
RUN apt-get update && \
    apt-get install -y cmake git ffmpeg libsm6 libxcb-xinerama0 libxext6 libglib2.0-0 lightdm python3.8 python3-pip python3-venv

RUN echo "/usr/sbin/lightdm" > /etc/X11/default-display-manager
RUN echo "\
[LightDM]\n\
[Seat:*]\n\
type=xremote\n\
xserver-hostname=host.docker.internal\n\
xserver-display-number=0\n\
autologin-user=root\n\
autologin-user-timeout=0\n\
autologin-session=Lubuntu\n\
" > /etc/lightdm/lightdm.conf.d/lightdm.conf

ENV DISPLAY=host.docker.internal:0.0

# Install the virtualenv python package
RUN python3 -m pip install --user virtualenv

# Create a virtual environment
RUN cd /opt && \
    python3 -m venv env

# Clone the N-Body-Simulations repository
RUN cd /usr && \
    git clone $GIT_REPOSITORY

# Activate python environment, and install the N-Body-Simulations package
RUN . /opt/env/bin/activate && \
    cd /usr/N-Body-Simulations && \
	pip install -r requirements.txt && \
	python3 setup.py install

CMD service dbus start; service lightdm start

CMD . /opt/env/bin/activate && python3 /usr/start.py
