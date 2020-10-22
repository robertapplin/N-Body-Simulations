# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from n_body_simulations.error_catcher import catch_errors

from PyQt5.QtCore import QCoreApplication


# Required to allow silent error catching
QCoreApplication.setApplicationName("test")


class DummyClass:
    """A class used for testing the error catcher by causing various errors and exceptions."""

    def __init__(self):
        pass

    def cause_an_uncaught_exception(self):
        raise RuntimeError("This is a RuntimeError.")

    @catch_errors()
    def cause_an_exception(self):
        raise RuntimeError("This is a RuntimeError.")

    @catch_errors()
    def divide_by_zero(self):
        return 10 / 0

    @catch_errors()
    def index_out_of_range(self):
        test_list = [0, 1, 2, 3]
        return test_list[4]

    @catch_errors()
    def function_that_returns_nothing(self):
        _ = 1 + 2

    @catch_errors()
    def function_that_returns_a_value(self):
        return 1.0


@pytest.fixture(scope='module')
def dummy_class():
    return DummyClass()


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
