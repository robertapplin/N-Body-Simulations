# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
from n_body_simulations.main_gui import start_gui
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

enable_test_mode()


def test_that_the_interface_opens_without_an_error():
    # Attempts to open the main interface
    start_gui()
