# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020

# Copy the input file to an output file in the build directory
configure_file(CMakeLists.txt.in "${CMAKE_BINARY_DIR}/googletest-download/CMakeLists.txt")

# Generate the googletest files
execute_process(COMMAND "${CMAKE_COMMAND}" -G "${CMAKE_GENERATOR}" .
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/googletest-download"
)

# Build googletest
execute_process(COMMAND "${CMAKE_COMMAND}" --build .
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/googletest-download"
)

# Prevent googletest from overriding our compiler/linker options
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# EXCLUDE_FROM_ALL prevents the install step occuring for googletest
add_subdirectory("${CMAKE_BINARY_DIR}/googletest-src"
                 "${CMAKE_BINARY_DIR}/googletest-build" EXCLUDE_FROM_ALL
)
