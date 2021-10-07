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
<<<<<<< HEAD
        self.bounds = np.array(args)
=======
        self.bounds = args
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a

    def __str__(self):
        """[summary] BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [str]: [description of the Box's bounds]
        """
<<<<<<< HEAD
        shape = (self.bounds).shape
        representation = "BoxWindow: "
        for i in range(shape[0] - 1):
            representation = representation + str((self.bounds)[i]) + " x "

        representation = representation + str((self.bounds)[shape[0] - 1])
        return representation

    def __len__(self):

        return len(self.bounds)

    def __contains__(self, args):
        VALUE = True
        for i in range(len(self.bounds)):
            if not (self.bounds[i][0] <= args[i] <= self.bounds[i][1]):
                VALUE = False

        return VALUE
=======

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
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a

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
=======
        """[summary]
        This method is similar to the method __len__ described above
        """
        return self.__len__()  # ? why not using use len(self)
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a

    # todo write tests
    def volume(self):
<<<<<<< HEAD
        """[summary]"""
        return
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
=======
        """[summary]
        This method calculates the volume of the Box
        """
        v = 1
        # * exploit numpy vectors, use - or np.diff, and np.prod
        for i in range(self.dimension()):
            # * use *= operator
            v = v * abs((self.bounds[i][1] - self.bounds[i][0]))

        return v
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a

    def indicator_function(self, args):
        """[summary]
        This method is similar to the method  __contains__  described above

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the box , False if not]
        """
        # ? isn't it equivalent to return args in self
        if self.__contains__(args):
            return True
        else:
            return False

    def center(self):
        """[summary] determinate the center of the box

        Returns:
            [numpy array list]: [the center of the box]
        """
<<<<<<< HEAD
=======
        # * Nice try!
        # ? how about np.mean(self.bounds)
        c = np.zeros(self.__len__())
        for i in range(self.__len__()):
            c[i] = np.mean(self.bounds[i])
        return c
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a

        return BoxWindow.__contains__(self, args)

    # def rand(self, n=1, rng=None):
    def rand(self, n=1, rng=None):
        """[summary]
        Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.

        Returns:
            Randomly n elements that belong to the box
        """
<<<<<<< HEAD
        X = np.zeros(shape=(n,))
        for i in range(len(self.bounds)):
            X[i] = get_random_number_generator(rng)
        return X
=======
        rng = get_random_number_generator(rng)
        # ? readability why not using self.dimension()
        L = np.ones((n, self.__len__()))  # liste des points
        # * exploit numpy, rng.uniform(a, b, size=n)
        for i in range(n):
            for j in range(self.__len__()):
                x = rng.random()

                L[i][j] = (1 - x) * self.bounds[j][0] + x * self.bounds[j][1]

        return L
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]a subclass of BoxWindow,represents the notion of "unit square box"

        Args:
            dimension ([int]): [dimension of the Unit Box]
            center ([numpy array list], optional): [center of the Box].
        """
        # * exploit numpy vectors, use - or np.diff, and +
        self.bounds = np.array(
            [[center[i] - 0.5, center[i] + 0.5] for i in range(dimension)]
        )
        super().__init__(self.bounds)  # * Nice call to super


# todo write tests
class BallWindow:
    """[summary]BoxWindow class representing a virtual n-dimensional bounded Box"""

    def __init__(self, center, radius, dimension):
        """[summary]Initialization of Box's parameters

        Args:
            args ([numpy array list]): [this argument represents the bounds of the box]
        """
        self.dim = dimension
        self.rad = radius
        self.cent = center

    def __contains__(self, args):
        """[summary]This method tests if an element (args) is inside the ball

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the ball , False if not]
        """
        # * same remarks as in BoxWindow.__contains__
        flag = True
        if len(args) != self.dim:
            return False
        else:
            if np.linalg.norm(args - self.center) <= self.rad:
                flag = True

        return flag

    def dimension(self):
        """[summary]
        This method gives the dimension of the ball
        """
        return self.dim

    def volume(self):
        r"""[summary]
        This method calculates the volume of the Ball using the formula :math:` V_{n+1} =\int_{-r}^{r}V_{n}(\sqrt{r^2 -x^2})dx`
        """
        # * iteresting recursive try
        # todo test the method
        # * exploit numpy vectors, use - or np.diff, and np.prod
        v = 1
        for i in range(self.dimension()):
            integ = lambda x: v * np.sqrt(self.rad ** 2 - x ** 2)
            v = integrate.quad(integ, -self.rad, self.rad)  # ! integrate is not defined

        return v

    def indicator_function(self, args):
        """[summary]
        This method is similar to the method  __contains__  described above

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the ball , False if not]
        """
        # ? isn't it equivalent to return args in self
        if self.__contains__(args):
            return True
        else:
            return False

    def center(self):
        """[summary] determinate the center of the ball

        Returns:
            [numpy array list]: [the center of the ball]
        """
<<<<<<< HEAD
<<<<<<< HEAD
        super(BoxWindow, self).__init__(args)
        for i in range(len(self.bounds)):
            X[i] = get_random_number_generator(rng)
        return X
=======
        super(UnitBoxWindow, self).__init__(bounds)
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
=======
        # * interesting try
        # * exploit numpy vectorization power
        # ? how about np.mean(self.bounds)
        c = np.zeros(self.__len__())
        for i in range(self.__len__()):
            c[i] = np.mean(self.bounds[i])
        return c
>>>>>>> 0c15242accca009adc793de993ed878c78c66c5a
