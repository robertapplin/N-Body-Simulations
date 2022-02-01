#####
## Docker image for N-Body-Simulations
#####

# Install the Ubuntu latest base image
FROM ubuntu:latest

# To avoid user interaction during the installation of cmake
ARG DEBIAN_FRONTEND=noninteractive

# Create git repository variable
ARG GIT_REPOSITORY=https://github.com/robertapplin/N-Body-Simulations

# Set the DISPLAY variable to be available at runtime
ENV DISPLAY=host.docker.internal:0.0

# Install packages required in the container environment
RUN apt-get update && \
    apt-get install -y cmake git libxcb-xinerama0 lightdm python3.8 python3-pip python3-venv

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

# Activate python environment, and startup the widget
CMD . /opt/env/bin/activate && \
    python3 /usr/N-Body-Simulations/n_body_simulations/startup.py
