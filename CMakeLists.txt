# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
cmake_minimum_required(VERSION 3.12)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(NBodySimulations)

set(SOURCE_DIRECTORY ${CMAKE_SOURCE_DIR}/cpp/simulator/src/)
set(HEADER_DIRECTORY ${CMAKE_SOURCE_DIR}/cpp/simulator/inc/)
set(PYTHON_DIRECTORY ${CMAKE_SOURCE_DIR}/python/)
set(EXPORT_DIRECTORY ${CMAKE_SOURCE_DIR}/python/exports/)
set(TEST_HELPER_DIRECTORY ${CMAKE_SOURCE_DIR}/tests/helpers/)

include_directories(${HEADER_DIRECTORY})

add_subdirectory(external)

add_subdirectory(cpp)
add_subdirectory(python)
add_subdirectory(tests)
