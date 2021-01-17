# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(SOURCE_FILES
    Body.cpp
    BodyPositionsAndVelocities.cpp
    NBodySimulator.cpp
    SimulationConstants.cpp
    Vector2D.cpp
)

set(HEADER_FILES
    Body.h
    BodyPositionsAndVelocities.h
    NBodySimulator.h
    SimulationConstants.h
    Vector2D.h
)

set(EXPORT_FILES
    nbodysimulations.cpp
    NBodySimulator.cpp
    Vector2D.cpp
)

list(TRANSFORM SOURCE_FILES PREPEND ${SOURCE_DIRECTORY})
list(TRANSFORM HEADER_FILES PREPEND ${HEADER_DIRECTORY})
list(TRANSFORM EXPORT_FILES PREPEND ${EXPORT_DIRECTORY})

# Creates a MODULE library which cannot be target-linked, but can be installed for python.
find_package(pybind11 REQUIRED)
pybind11_add_module(NBodySimulations
                    MODULE
                    ${SOURCE_FILES}
                    ${HEADER_FILES}
                    ${EXPORT_FILES}
)

# Creates a STATIC library which can be target-linked, and therefore tested.
add_library(NBodySimulationsTestable
            STATIC
            ${SOURCE_FILES}
            ${HEADER_FILES}
)

target_link_libraries(NBodySimulations PUBLIC)
target_link_libraries(NBodySimulationsTestable PUBLIC)

install(TARGETS NBodySimulations
        COMPONENT python
        LIBRARY DESTINATION "${PYTHON_LIBRARY_DIR}"
)
