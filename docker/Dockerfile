#####
## Docker image for N-Body-Simulations
#####

# Install the Ubuntu latest base image
FROM ubuntu:latest

# To avoid user interaction during the installation of cmake
ARG DEBIAN_FRONTEND=noninteractive

# Create git repository variable
ARG GIT_REPOSITORY=https://github.com/robertapplin/N-Body-Simulations

# Set DISPLAY environment variable
ENV DISPLAY=host.docker.internal:0.0

# Set environment variables to avoid warnings
ENV LIBGL_ALWAYS_INDIRECT=1
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# Install packages required in the container environment. Then clean up the apt cache
RUN apt-get update && \
    apt-get install -y cmake git libgl1-mesa-glx libxcb-xinerama0 lightdm mesa-utils python3.8 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Copy config files into the container
COPY config/lightdm.conf /etc/lightdm/lightdm.conf.d/lightdm.conf
COPY config/default-display-manager /etc/X11/default-display-manager

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
