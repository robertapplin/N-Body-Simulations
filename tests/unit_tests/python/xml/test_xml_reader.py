# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.xml_reader import get_user_interface_property
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

enable_test_mode()


def test_that_get_user_interface_property_returns_a_valid_property_from_the_user_property_file():
    mass_step = get_user_interface_property("mass-step")
    assert mass_step == "0.1"


def test_that_get_user_interface_property_raises_an_error_when_the_property_name_is_invalid():
    try:
        _ = get_user_interface_property("invalid-property")
        pytest.fail("This should have failed.")
    except ValueError as error:
        assert str(error) == "The item 'invalid-property' does not exist in the file ':/user-interface-properties.xml'."
