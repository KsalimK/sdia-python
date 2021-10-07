import numpy as np

from lab2.utils import get_random_number_generator
import numpy as np


class Myclass(object):
    def __init__(self, args):
        self.arg = arg


# todo clean up the docstrings
class BoxWindow:
    """[summary]BoxWindow class representing a virtual n-dimensional bounded Box"""

    def __init__(self, args):
        """[summary]Initialization of Box's parameters

        Args:
            args ([numpy array list]): [this argument represents the bounds of the box]
        """
        self.bounds = args

    def __str__(self):
        """[summary] BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [str]: [description of the Box's bounds]
        """

        shape = (self.bounds).shape
        representation = "BoxWindow: "
        # * consider for a, b in self.bounds
        # ! use f-strings
        for i in range(shape[0] - 1):  # ? why not self.dimension()
            representation = (
                representation
                + "["
                + str((self.bounds)[i][0])
                + ", "
                + str((self.bounds)[i][1])
                + "]"
                + " x "
            )

        representation = (
            representation
            + "["
            + str((self.bounds)[shape[0] - 1][0])
            + ", "
            + str((self.bounds)[shape[0] - 1][1])
            + "]"
        )

        return representation

    def __len__(self):
        """[summary]

        Returns:
            [int: [the dimension of the box]
        """
        return ((self.bounds).shape)[0]  # * no need to use ()

    def __contains__(self, args):
        """[summary]This method tests if an element (args) is inside the box

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the box , False if not]
        """
        # * consider for (a, b), x in zip(self.bounds, point)
        # * or exploit numpy vectorization power
        flag = True
        for i in range(self.__len__()):  # ? use len(self) of self.dimension
            if args[i] >= self.bounds[i][0] and args[i] <= self.bounds[i][1]:
                flag = True
            else:
                return False

        return flag  # ? flag is never modified and always returns True

    # todo write tests
    def dimension(self):
<<<<<<< HEAD
<<<<<<< HEAD
        """[summary]
        """
        return self.bounds.shape()

    def volume(self):
        """[summary]
        """
        VALUE = 1
        for i in range(len(self.bounds)):
            VALUE *= abs(self.bounds[i][0] - self.bounds[i][1])
        return VALUE
=======
        """[summary]"""
        return
