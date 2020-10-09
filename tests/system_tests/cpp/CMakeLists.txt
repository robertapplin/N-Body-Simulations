# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(TEST_FILES
    NBodySimulatorTest.cpp
)

find_package(GTest REQUIRED)

add_executable(NBodySimulationsSystemTests main.cpp ${TEST_FILES})

target_include_directories(NBodySimulationsSystemTests
                           PRIVATE
                           ${GTEST_INCLUDE_DIR}
)

target_link_libraries(NBodySimulationsSystemTests 
                      PRIVATE
                      GTest::GTest
)