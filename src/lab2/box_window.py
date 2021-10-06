from lab2.utils import get_random_number_generator
import numpy as np


class Myclass(object):
    def __init__(self, args):
        self.arg = arg


class BoxWindow:
    """[summary]
    """

    def __init__(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        self.bounds = np.array(args)

    def __repr__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
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

    def dimension(self):
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

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """

        return BoxWindow.__contains__(self, args)

    # def rand(self, n=1, rng=None):
    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        X = np.zeros(shape=(n,))
        for i in range(len(self.bounds)):
            X[i] = get_random_number_generator(rng)
        return X


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
        for i in range(len(self.bounds)):
            X[i] = get_random_number_generator(rng)
        return X
