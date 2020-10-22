# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(PYTHON_FILES
    ${CMAKE_SOURCE_DIR}/python/startup.py
    ${CMAKE_SOURCE_DIR}/python/qt/add_body_dialog.py
    ${CMAKE_SOURCE_DIR}/python/qt/error_catcher.py
    ${CMAKE_SOURCE_DIR}/python/qt/main_gui.py
    ${CMAKE_SOURCE_DIR}/python/qt/model.py
    ${CMAKE_SOURCE_DIR}/python/qt/presenter.py
    ${CMAKE_SOURCE_DIR}/python/qt/view.py
    ${CMAKE_SOURCE_DIR}/python/qt/ui/add_body_dialog_ui.py
    ${CMAKE_SOURCE_DIR}/python/qt/ui/main_window_ui.py
    ${CMAKE_SOURCE_DIR}/python/plotting/interactive_plot.py
    ${CMAKE_SOURCE_DIR}/python/plotting/simulation_animator.py
)

install(FILES ${PYTHON_FILES}
        DESTINATION "${PYTHON_LIBRARY_DIR}/n_body_simulations"
)
