import numpy as np

from sdia_python.lab2.ball_window import BallWindow


class UnitBallWindow(BallWindow):
    def __init__(self, center):
        """a subclass of BoxWindow,represents the notion of "unit square box"

        Args:
            dimension (int): dimension of the Unit Box
            center (array, optional): center of the Box.
        """

        self.rad = 1
        self.cent = center

        super().__init__(center=self.cent, radius=self.rad)
