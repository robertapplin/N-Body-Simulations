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
file(GLOB PYTHON_FILES "python/exports/*.cpp")

find_package(pybind11 REQUIRED)
pybind11_add_module(nbodysimulations
	${SOURCE_FILES}
	${HEADER_FILES}
	${PYTHON_FILES}
)

target_link_libraries(nbodysimulations PUBLIC)

install(TARGETS nbodysimulations
  COMPONENT python
  LIBRARY DESTINATION "${PYTHON_LIBRARY_DIR}"
  )