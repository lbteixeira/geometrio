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
            if not self.point.is_at_right(edge):
                N += 1

        if N % 2 != 0:
            self.is_included = True

        print(N)
        return is_included


if __name__ == "__main__":
    point = Point(0.5, 0.5)
    v1 = Point(0.0, 0.0)
    v2 = Point(1.0, 1.0)
    v3 = Point(1.0, 0.0)
    v4 = Point(0.0, 1.0)

    l1 = Line(v1, v3)
    l2 = Line(v1, v4)
    l3 = Line(v2, v3)
    l4 = Line(v2, v4)

    polygon = Polygon([l1, l2, l3, l4])

    checker = InclusionChecker(point, polygon)
    is_included = checker.point_inclusion()
