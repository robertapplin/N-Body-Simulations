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
    apt-get install -y git wget && \
    rm -rf /var/lib/apt/lists/*

# Download and install conda
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

ARG PATH="/root/miniconda3/bin:${PATH}"

# Copy config files into the container
#COPY config/lightdm.conf /etc/lightdm/lightdm.conf.d/lightdm.conf
#COPY config/default-display-manager /etc/X11/default-display-manager

# Clone the N-Body-Simulations repository
RUN cd /usr && \
    git clone $GIT_REPOSITORY

# Initialize conda and create an environment
RUN cd /usr/N-Body-Simulations && \
    conda init && \
    conda env create -f conda/testing.yml

# Activate conda environment, and install the N-Body-Simulations package
SHELL ["conda", "run", "-n", "n-body-env", "python", "/usr/N-Body-Simulations/setup.py", "install"]
