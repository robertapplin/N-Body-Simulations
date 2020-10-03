# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest
import sys
from directory_helper import PYTHON_DIRECTORY

# Required to find python modules in parent directories
sys.path.append(PYTHON_DIRECTORY)

from qt.error_catcher import catch_errors


class ErrorCauser:
    """A class used for testing the error catcher by causing various errors and exceptions."""

    def __init__(self):
        pass

    def cause_an_uncaught_exception(self):
        raise RuntimeError("This is a RuntimeError.")

    @catch_errors(silent=True)
    def cause_an_exception(self):
        raise RuntimeError("This is a RuntimeError.")

    @catch_errors(silent=True)
    def divide_by_zero(self):
        return 10 / 0

    @catch_errors(silent=True)
    def index_out_of_range(self):
        test_list = [0, 1, 2, 3]
        return test_list[4]


@pytest.fixture(scope='module')
def error_causer():
    return ErrorCauser()


def test_that_the_error_causer_causes_an_error_when_not_using_the_error_catcher(error_causer):
    try:
        error_causer.cause_an_uncaught_exception()
    except RuntimeError:
        return
    pytest.fail("The ErrorCauser class did not cause an exception when expected.")


def test_that_an_exception_is_caught_by_the_error_catcher(error_causer):
    error_causer.cause_an_exception()


def test_that_a_divide_by_zero_error_is_caught_by_the_error_catcher(error_causer):
    error_causer.divide_by_zero()


def test_that_an_index_out_of_range_error_is_caught_by_the_error_catcher(error_causer):
    error_causer.index_out_of_range()
