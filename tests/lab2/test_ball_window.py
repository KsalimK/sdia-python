import numpy as np
import pytest

from lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([2.5, 2.5]), 3, "BallWindow: [2.5 2.5], 3"),
        (np.array([0.5, 2, 5.5]), 5, "BallWindow: [0.5 2.  5.5], 5"),
        (np.array([1, 2, 3, 4]), 2, "BallWindow: [1 2 3 4], 2",),
    ],
)
def test_ball_string_representation(center, radius, expected):
    assert (BallWindow(center, radius)).__str__() == expected


@pytest.fixture
def ball_2d_05():
    return BallWindow(center=np.array([0.5, 0.5]), radius=3)


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_ball_2d(ball_2d_05, point, expected):
    is_in = ball_2d_05.indicator_function(point)
    assert is_in == expected


######################################test dimension###########################
@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0, 0]), 3, 2),
        (np.array([2.5, 2.5]), 2, 2),
        (np.array([1, 2, 3]), 2, 3),
        (np.array([1, 2, 3, 4, 5]), 1, 5),
    ],
)
def test_dimension(center, radius, expected):
    box = BallWindow(center, radius)
    assert np.array_equal(box.dimension(), expected)


#######################################test volume##############################
@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0, 0]), 3, np.pi * (3 ** 2)),
        (np.array([2.5, 2.5]), 2, np.pi * (2 ** 2)),
        (np.array([1, 2, 3]), 2, 4 * np.pi * (2 ** 3) / 3),
        (np.array([0.5, 0, 2]), 1, 4 * np.pi * (1 ** 3) / 3),
    ],
)
def test_volume(center, radius, expected):
    box = BallWindow(center, radius)
    assert np.array_equal(box.volume(), expected)
