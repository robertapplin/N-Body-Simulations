#!/usr/bin/env bash

# Create a directory for storing artifacts
mkdir artifacts

# Get the current date in YYYY-MM-DD
printf -v date '%(%Y-%m-%d)T' -1 

# Store the list of conda dependencies in a *.txt file
filepath_list=${GITHUB_WORKSPACE}"/dependency-list-"${date}".txt"
conda list > $filepath_list

# Store a diff of the conda dependencies compared to the previous dependency list
filepath_diff=${GITHUB_WORKSPACE}"/artifacts/dependency-diff-"${date}".txt"
git diff dependency-list.txt $filepath_list > $filepath_diff
