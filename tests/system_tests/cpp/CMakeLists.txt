# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(TEST_FILES
    NBodySimulatorTest.cpp
)

add_executable(NBodySimulationsSystemTests main.cpp ${TEST_FILES})

target_link_libraries(NBodySimulationsSystemTests
                      PRIVATE
                      gtest
                      NBodySimulationsTestable
)
