import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


class BoxWindow:
    """BoxWindow class representing a virtual n-dimensional bounded Box"""

    def __init__(self, args):
        """Initialization of Box's parameters

        Args:
            args (array): this argument represents the bounds of the box
        """
        self.bounds = args

    def __str__(self):
        """ BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: description of the Box's bounds
        """

        shape = self.bounds.shape
        representation = "BoxWindow: "

        for i in range(self.dimension() - 1):

            representation = (
                representation + f"[{(self.bounds)[i][0]}, {(self.bounds)[i][1]}] x "
            )
        representation = (
            representation
            + f"[{(self.bounds)[self.dimension() - 1][0]}, {(self.bounds)[self.dimension() - 1][1]}]"
        )

        return representation

    def __len__(self):
        """Similar to dimension determination

        Returns:
            int: the dimension of the box
        """
        return self.bounds.shape[0]

    def __contains__(self, args):
        """This method tests if an element (args) is inside the box

        Args:
            args (array): the element to test

        Returns:
            bool: True if the element is inside the box , False if not
        """

        return np.all(
            np.concatenate((args >= self.bounds[:, 0], args <= self.bounds[:, 1]))
        )

    def dimension(self):
        """This method is similar to the method __len__ described above
        """
        return len(self)

    def volume(self):
        """This method calculates the volume of the Box
        """

        return np.prod(abs(self.bounds[:, 1] - self.bounds[:, 0]))

    def indicator_function(self, args):
        """This method is similar to the method  __contains__  described above

        Args:
            args (array): the element to test

        Returns:
            bool: True if the element is inside the box , False if not
        """

        return self.__contains__(args)

    def center(self):
        """Determinate the center of the box

        Returns:
            array: the center of the box
        """

        return np.mean(self.bounds, axis=1)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional):  Defaults to 1.
            rng (object, optional):  Defaults to None.

        Returns:
            Randomly n elements that belong to the box
        """

        rng = get_random_number_generator(rng)
        p = rng.uniform(self.bounds[0, 0], self.bounds[0, 1], size=(n, 1))
        for j in range(1, self.dimension()):
            p = np.hstack(
                (p, rng.uniform(self.bounds[j, 0], self.bounds[j, 1], size=(n, 1)))
            )
        return p
