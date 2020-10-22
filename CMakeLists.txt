# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
cmake_minimum_required(VERSION 3.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(NBodySimulations)

set(SOURCE_DIRECTORY ${CMAKE_SOURCE_DIR}/cpp/simulator/src)
set(HEADER_DIRECTORY ${CMAKE_SOURCE_DIR}/cpp/simulator/inc)
set(EXPORT_DIRECTORY ${CMAKE_SOURCE_DIR}/python/exports)

include_directories(${HEADER_DIRECTORY})

add_subdirectory(external)

add_subdirectory(cpp)
add_subdirectory(python)
add_subdirectory(tests)
