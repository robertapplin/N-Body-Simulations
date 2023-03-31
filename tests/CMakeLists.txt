# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
find_package(GTest 1.13 REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_subdirectory(system_tests)
add_subdirectory(unit_tests)
