#!/usr/bin/env bash
set -ex

mkdir build && cd build

cmake --preset=ninja \
    -DPYTHON_EXECUTABLE=$PYTHON \
    -Dpybind11_DIR=$PREFIX/share/cmake/pybind11 \
    -DCMAKE_INSTALL_PREFIX=$PREFIX \
    -DCMAKE_INSTALL_LIBDIR=$SP_DIR \
    ../

ninja
ninja install

cd ../
$PYTHON -m pip install --ignore-installed .
