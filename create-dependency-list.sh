#!/usr/bin/env bash

# Create a directory for storing artifacts
mkdir artifacts

# Get the current date in YYYY-MM-DD
printf -v date '%(%Y-%m-%d)T' -1 

# Store the list of conda dependencies in a *.txt file
filepath="./artifacts/dependency-list-"${date}".txt"
conda list > $filepath
