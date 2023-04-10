#!/usr/bin/env bash

if test -f $GITHUB_WORKSPACE/cache/dependency-list.txt; then
  mv $GITHUB_WORKSPACE/cache/dependency-list.txt $GITHUB_WORKSPACE/dependency-list.txt
else
  touch $GITHUB_WORKSPACE/dependency-list.txt
fi
