import numpy as np

from sdia_python.lab2.box_window import BoxWindow


class UnitBoxWindow(BoxWindow):
    def __init__(self, center):
        """a subclass of BoxWindow,represents the notion of "unit square box"

        Args:
            dimension (int): dimension of the Unit Box
            center (array, optional): center of the Box.
        """
        self.bounds = np.column_stack((center - 0.5, center + 0.5))

        super().__init__(self.bounds)
