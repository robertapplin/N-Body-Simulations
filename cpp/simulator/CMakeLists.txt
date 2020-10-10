# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(SOURCE_FILES
    ${SOURCE_DIRECTORY}/Body.cpp
    ${SOURCE_DIRECTORY}/NBodySimulator.cpp
    ${SOURCE_DIRECTORY}/SimulationConstants.cpp
    ${SOURCE_DIRECTORY}/SpaceTimeBodyCoords.cpp
    ${SOURCE_DIRECTORY}/Vector2D.cpp
)

set(HEADER_FILES
    ${HEADER_DIRECTORY}/Body.h
    ${HEADER_DIRECTORY}/NBodySimulator.h
    ${HEADER_DIRECTORY}/SimulationConstants.h
    ${HEADER_DIRECTORY}/SpaceTimeBodyCoords.h
    ${HEADER_DIRECTORY}/Vector2D.h
)

set(EXPORT_FILES
    ${EXPORT_DIRECTORY}/NBodySimulations.cpp
    ${EXPORT_DIRECTORY}/NBodySimulator.cpp
    ${EXPORT_DIRECTORY}/Vector2D.cpp
)

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
