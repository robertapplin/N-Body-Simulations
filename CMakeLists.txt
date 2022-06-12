# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
cmake_minimum_required(VERSION 3.12)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(NBodySimulations)

# Setup ccache if it can be found. Used only for the Ninja generator
find_program(CCACHE_FOUND ccache)
if(CCACHE_FOUND)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE ccache)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK ccache)
endif()

set(SOURCE_DIRECTORY ${CMAKE_SOURCE_DIR}/cpp/simulator/src/)
set(HEADER_DIRECTORY ${CMAKE_SOURCE_DIR}/cpp/simulator/inc/)
set(EXPORT_DIRECTORY ${CMAKE_SOURCE_DIR}/n_body_simulations/exports/)
set(TEST_HELPER_DIRECTORY ${CMAKE_SOURCE_DIR}/tests/helpers/)

include_directories(${HEADER_DIRECTORY})

add_subdirectory(cpp)
add_subdirectory(tests)
