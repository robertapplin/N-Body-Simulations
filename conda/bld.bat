mkdir build && cd build

cmake ^
    -DPYTHON_EXECUTABLE="%PYTHON%" ^
    -Dpybind11_DIR=%LIBRARY_PREFIX%/share/cmake/pybind11 ^
    -DCMAKE_INSTALL_PREFIX=%LIBRARY_PREFIX% ^
    -DCMAKE_INSTALL_LIBDIR=%SP_DIR% ^
    -G Ninja ^
    ..

if errorlevel 1 exit 1
cmake --build . --config Release
cmake --build . --config Release --target install
if errorlevel 1 exit 1

cd ../
"%PYTHON%" -m pip install --ignore-installed .
if errorlevel 1 exit 1
