from ..primitives.primitives import Point, Polygon, Line


class InclusionChecker():
    """Class containing methods to check if a point is included in a
    polygon."""

    point: Point
    polygon: Polygon

    def __init__(self, point: Point, polygon: Polygon):
        self.point = point
        self.polygon = polygon

    def point_inclusion(self):
        N = 0
        is_included = False
        for edge in self.polygon.edges:

            ordered_points = edge.order_points()
            a = ordered_points[0]
            b = ordered_points[1]

            if a.coord_y < self.point.coord_y and b.coord_y > self.point.coord_y and \
                self.point.is_at_right(edge):
                N += 1

        if N % 2 != 0:
            is_included = True

        return is_included
