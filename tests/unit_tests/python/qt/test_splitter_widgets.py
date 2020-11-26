# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import qtawesome as qta

from n_body_simulations.splitter_widgets import Splitter
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

enable_test_mode()


def test_that_creating_a_Splitter_with_an_icon_does_not_raise_an_exception():
    _ = Splitter(qta.icon('mdi.dots-horizontal', scale_factor=1.0))
