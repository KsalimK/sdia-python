import numpy as np
import pytest

from lab2.box_window import BoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0 5] x [0 5]"),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
<<<<<<< HEAD
            "BoxWindow: [0 5] x [-1.45 3.14] x [-10 10]",
=======
            "BoxWindow: [0.0, 5.0] x [-1.45, 3.14] x [-10.0, 10.0]",
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a
        ),
    ],
)
def test_box_string_representation(bounds, expected):
<<<<<<< HEAD
<<<<<<< HEAD
    A = BoxWindow(bounds)
    str_repr = BoxWindow.__repr__(A)
    assert str_repr == expected
=======
    assert str(BoxWindow(bounds)) == expected
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
=======
    assert (BoxWindow(bounds)).__str__() == expected
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


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
    is_in = BoxWindow.indicator_function(box_2d_05, point)
    assert is_in == expected


# is_in = box_2d_05.indicator_function(point)
# for i,x in enumerate(point)

# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================
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
    box = BoxWindow(bounds)
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
    box = BoxWindow(bounds)
    assert all_in(box, n) == expected
