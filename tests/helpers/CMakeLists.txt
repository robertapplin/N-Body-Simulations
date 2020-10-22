# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(HELPER_FILES
    dummy_class_helper.py
    setup_test_helper.py
)

list(TRANSFORM HELPER_FILES PREPEND ${TEST_HELPER_DIRECTORY})

install(FILES ${HELPER_FILES}
        DESTINATION "${PYTHON_LIBRARY_DIR}/n_body_simulations/test_helpers"
)
