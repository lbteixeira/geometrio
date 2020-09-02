from typing import Tuple

class Line:

    point1: Tuple
    point2: Tuple

    def __init__(self, point1: Tuple, point2: Tuple):
        self.point1 = point1
        self.point2 = point2
