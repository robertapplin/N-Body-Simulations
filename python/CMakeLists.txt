# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
set(PYTHON_FILES
    startup.py
    plotting/interactive_plot.py
    plotting/simulation_animator.py
    qt/add_body_dialog.py
    qt/error_catcher.py
    qt/main_gui.py
    qt/model.py
    qt/presenter.py
    qt/signal_blocker.py
    qt/view.py
    qt/ui/add_body_dialog_ui.py
    qt/ui/main_window_ui.py
)

list(TRANSFORM PYTHON_FILES PREPEND ${PYTHON_DIRECTORY})

install(FILES ${PYTHON_FILES}
        DESTINATION "${PYTHON_LIBRARY_DIR}/n_body_simulations"
)
