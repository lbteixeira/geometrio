from ..primitives.primitives import Point, Polygon


class InclusionChecker():
    """Class containing methods to check if point is included in a polygon."""

    point: Point
    polygon: Polygon

    def __init__(self, point: Point, polygon: Polygon):
        self.point = point
        self.polygon = polygon

    def point_inclusion(self):
        N = 0
        is_included = False
        for edge in self.polygon.lines:
            if not self.point.is_at_right(edge):
                N += 1

        if N % 2 != 0:
            self.is_included = True

        print(N)
        return is_included
