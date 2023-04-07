#!/usr/bin/env bash
set -ex

cmake --preset=ninja \
    -DPYTHON_EXECUTABLE=$PYTHON \
    -Dpybind11_DIR=$PREFIX/share/cmake/pybind11 \
    -DCMAKE_INSTALL_PREFIX=$PREFIX \
    -DCMAKE_INSTALL_LIBDIR=$SP_DIR \
    $SRC_DIR

cd ../build
ninja
ninja install

$PYTHON -m pip install --ignore-installed $SRC_DIR
