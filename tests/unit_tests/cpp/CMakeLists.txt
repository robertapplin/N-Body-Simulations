# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(TEST_FILES
    BodyPositionsAndVelocitiesTest.cpp
    BodyTest.cpp
    NBodySimulatorTest.cpp
    SimulationConstantsTest.cpp
    Vector2DTest.cpp
)

add_executable(NBodySimulationsUnitTests main.cpp ${TEST_FILES})

target_link_libraries(NBodySimulationsUnitTests
                      PRIVATE
                      ${GTEST_BOTH_LIBRARIES}
                      NBodySimulationsTestable
)
