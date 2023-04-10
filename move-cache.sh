#!/usr/bin/env bash

if test -f $GITHUB_WORKSPACE/cache/dependency-list.txt; then
  echo "Found dependency cache"
  mv $GITHUB_WORKSPACE/cache/dependency-list.txt $GITHUB_WORKSPACE/dependency-list.txt
else
  echo "No dependency cache found"
  touch $GITHUB_WORKSPACE/dependency-list.txt
fi
