import numpy as np
import pytest

from sdia_python.lab2.unit_box_window import UnitBoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "center, expected",
    [
        (np.array([2.5]), "BoxWindow: [2.0, 3.0]"),
        (
            np.array([0.5, 1, 2, 4]),
            "BoxWindow: [0.0, 1.0] x [0.5, 1.5] x [1.5, 2.5] x [3.5, 4.5]",
        ),
        (np.array([1, 10, 2]), "BoxWindow: [0.5, 1.5] x [9.5, 10.5] x [1.5, 2.5]",),
    ],
)
def test_box_string_representation(center, expected):
    assert (UnitBoxWindow(center)).__str__() == expected


@pytest.fixture
def box_2d_05():
    return UnitBoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


#######################################test center##############################
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 0]]), np.array([0])),
        (np.array([[2.5, 2.5]]), np.array([2.5])),
        (np.array([[1, 3], [5, 7]]), np.array([2, 6])),
        (np.array([[1, 3], [5, 7], [10, 20]]), np.array([2, 6, 15])),
    ],
)
def test_center(bounds, expected):
    box = UnitBoxWindow(bounds)
    assert np.array_equal(box.center(), expected)


######################################test rand#################################
def all_in(box, n):
    flag = True
    for i in range(n):
        flag = box.indicator_function(box.rand(n)[i])

    return flag


@pytest.mark.parametrize(
    "bounds,n,expected",
    [
        (np.array([[1, 2]]), 1, True),
        (np.array([[1, 2], [1, 2]]), 2, True),
        (np.array([[1, 2], [100, 101]]), 3, True),
        (np.array([[1, 2], [4, 4]]), 4, True),
    ],
)
def test_rand_points_in_box(bounds, n, expected):
    box = UnitBoxWindow(bounds)
    assert all_in(box, n) == expected


#######################################test volume##############################
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 0]]), 0),
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[1, 3], [5, 7]]), 4),
        (np.array([[1, 3], [5, 7], [10, 20]]), 40),
    ],
)
def test_volume(bounds, expected):
    box = UnitBoxWindow(bounds)
    assert np.array_equal(box.volume(), expected)
