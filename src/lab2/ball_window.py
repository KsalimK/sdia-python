import numpy as np
import scipy.integrate as integrate

from lab2.box_window import BoxWindow


class BallWindow:
    """BoxWindow class representing a virtual n-dimensional bounded Box"""

    def __init__(self, center, radius):
        """Initialization of Box's parameters

        Args:
            args (array): this argument represents the bounds of the box
        """

        self.rad = radius
        self.cent = center

    def __str__(self):
        """Description of the Ball

        Returns:
            str: description of the Ball
        """
        return f"BallWindow: {self.cent}, {self.rad}"

    def __contains__(self, args):
        """This method tests if an element (args) is inside the ball

        Args:
            args (array): the element to test

        Returns:
            bool: True if the element is inside the ball , False if not
        """

        return np.all(abs(args - self.cent) < self.rad)

    def dimension(self):
        """This method gives the dimension of the ball
        """
        return len(self.cent)

    def volume(self):
        """This method calculates the volume of the Ball using the formula explained in the following link :https://fr.wikipedia.org/wiki/N-sph%C3%A8re
        """
        n = self.dimension()
        R = self.rad
        if n % 2 == 0:  # formula in case dimension is even
            return (((np.pi) ** (n / 2)) * R ** n) / np.math.factorial(n / 2)
        else:  # formula in case dimension is odd
            odds = [i for i in range(1, n + 1, 2)]
            product = np.product(odds)
            return 2 ** ((n + 1) / 2) * np.pi ** ((n - 1) / 2) * R ** n / product

    def indicator_function(self, args):
        """This method is similar to the method  __contains__  described above

        Args:
            args (array): the element to test

        Returns:
            bool: True if the element is inside the ball , False if not
        """

        return self.__contains__(args)
