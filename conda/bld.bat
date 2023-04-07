cmake --preset=vs-release ^
    -DPYTHON_EXECUTABLE="%PYTHON%" ^
    -Dpybind11_DIR=%LIBRARY_PREFIX%/share/cmake/pybind11 ^
    -DCMAKE_INSTALL_PREFIX=%LIBRARY_PREFIX% ^
    -DCMAKE_INSTALL_LIBDIR=%SP_DIR% ^
    %SRC_DIR%

if errorlevel 1 exit 1
cmake --build ../build --config Release
cmake --build ../build --config Release --target install
if errorlevel 1 exit 1

"%PYTHON%" -m pip install --ignore-installed %SRC_DIR%
if errorlevel 1 exit 1
