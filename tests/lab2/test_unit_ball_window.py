import numpy as np
import pytest

from sdia_python.lab2.unit_ball_window import UnitBallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "center, expected",
    [
        (np.array([2.5, 2.5]), "BallWindow: [2.5 2.5], 1"),
        (np.array([0.5, 2, 5.5]), "BallWindow: [0.5 2.  5.5], 1"),
        (np.array([1, 2, 3, 4]), "BallWindow: [1 2 3 4], 1",),
    ],
)
def test_ball_string_representation(center, expected):
    assert (UnitBallWindow(center)).__str__() == expected


@pytest.fixture
def ball_2d_05():
    return UnitBallWindow(center=np.array([0.5, 0.5]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), False),
        (np.array([-1, 5]), False),
        (np.array([1, 0]), True),
    ],
)
def test_indicator_function_ball_2d(ball_2d_05, point, expected):
    is_in = ball_2d_05.indicator_function(point)
    assert is_in == expected


######################################test dimension###########################
@pytest.mark.parametrize(
    "center, expected",
    [
        (np.array([0, 0]), 2),
        (np.array([2.5, 2.5]), 2),
        (np.array([1, 2, 3]), 3),
        (np.array([1, 2, 3, 4, 5]), 5),
    ],
)
def test_dimension(center, expected):
    box = UnitBallWindow(center)
    assert np.array_equal(box.dimension(), expected)


#######################################test volume##############################
@pytest.mark.parametrize(
    "center, expected",
    [
        (np.array([0, 0]), np.pi * (1 ** 2)),
        (np.array([2.5, 2.5]), np.pi * (1 ** 2)),
        (np.array([1, 2, 3]), 4 * np.pi * (1 ** 3) / 3),
        (np.array([0.5, 0, 2]), 4 * np.pi * (1 ** 3) / 3),
    ],
)
def test_volume(center, expected):
    box = UnitBallWindow(center)
    assert np.array_equal(box.volume(), expected)
