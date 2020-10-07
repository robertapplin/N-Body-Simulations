# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
cmake_minimum_required(VERSION 3.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

project(NBodySimulations)

include_directories("${CMAKE_SOURCE_DIR}/cpp/inc/inc")

file(GLOB SOURCE_FILES "cpp/simulator/src/*.cpp")
file(GLOB HEADER_FILES "cpp/simulator/inc/inc/*.h")
file(GLOB EXPORT_FILES "python/exports/*.cpp")
file(GLOB SYSTEM_TEST_SOURCE_FILES "tests/system_tests/cpp/*.cpp")
file(GLOB SYSTEM_TEST_HEADER_FILES "tests/system_tests/cpp/*.h")

add_library(NBodySimulationsSystemTests
            ${SYSTEM_TEST_SOURCE_FILES}
            ${SYSTEM_TEST_HEADER_FILES}
)

find_package(pybind11 REQUIRED)
pybind11_add_module(NBodySimulations
                    ${SOURCE_FILES}
                    ${HEADER_FILES}
                    ${EXPORT_FILES}
)

target_link_libraries(NBodySimulations PUBLIC)

install(TARGETS NBodySimulations
        COMPONENT python
        LIBRARY DESTINATION "${PYTHON_LIBRARY_DIR}"
)