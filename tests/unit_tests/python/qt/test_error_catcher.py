# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.test_helpers.dummy_class_helper import DummyErrorProneClass
from n_body_simulations.test_helpers.setup_test_helper import enable_test_mode

enable_test_mode()


@pytest.fixture(scope='module')
def dummy_class():
    return DummyErrorProneClass()


def test_that_the_error_causer_causes_an_error_when_not_using_the_error_catcher(dummy_class):
    try:
        dummy_class.cause_an_uncaught_exception()
    except RuntimeError:
        return
    pytest.fail("The ErrorCauser class did not cause an exception when expected.")


def test_that_an_exception_is_caught_by_the_error_catcher(dummy_class):
    dummy_class.cause_an_exception()


def test_that_a_divide_by_zero_error_is_caught_by_the_error_catcher(dummy_class):
    dummy_class.divide_by_zero()


def test_that_an_index_out_of_range_error_is_caught_by_the_error_catcher(dummy_class):
    dummy_class.index_out_of_range()


def test_that_a_function_returning_nothing_will_not_cause_an_error_when_decorated_by_the_error_catcher(dummy_class):
    dummy_class.function_that_returns_nothing()


def test_that_a_function_will_return_the_correct_value_when_decorated_by_the_error_catcher(dummy_class):
    assert dummy_class.function_that_returns_a_value() == 1.0
