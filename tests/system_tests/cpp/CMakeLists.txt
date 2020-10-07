# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(SOURCE_FILES
    fake.cpp
)

set(HEADER_FILES
    fake.h
)

add_library(NBodySimulationsSystemTests
            ${SOURCE_FILES}
            ${HEADER_FILES}
)