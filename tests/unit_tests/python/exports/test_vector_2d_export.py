# Project Repository : https://github.com/robertapplin/N-Body-Simulations
# Authored by Robert Applin, 2020
import pytest

from NBodySimulations import Vector2D


@pytest.fixture
def vector_2d():
    return Vector2D(1.0, 2.0)


def test_that_creating_a_Vector2D_does_not_raise():
    _ = Vector2D(1.0, 2.0)


def test_that_the_Vector2D_member_variables_are_exposed_to_python(vector_2d):
    assert vector_2d.x == 1.0
    assert vector_2d.y == 2.0


def test_that_the_is_equal_to_operator_for_Vector2D_is_exposed_to_python(vector_2d):
    assert vector_2d == vector_2d


def test_that_reassigning_Vector2D_member_variables_works_in_python(vector_2d):
    vector_2d.x = 3.0
    vector_2d.y = 4.0

    assert vector_2d == Vector2D(3.0, 4.0)
