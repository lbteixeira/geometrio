from geometrio.primitives.primitives import Line, Point, Polygon
from geometrio.inclusion.inclusion import InclusionChecker


def test_point_inclusion():
    point = Point(0.5, 0.5)
    v1 = Point(0.0, 0.0)
    v2 = Point(0.9, 0.9)
    v3 = Point(1.0, 0.1)
    v4 = Point(0.1, 1.1)

    l1 = Line(v1, v3)
    l2 = Line(v1, v4)
    l3 = Line(v2, v3)
    l4 = Line(v2, v4)

    polygon = Polygon([l1, l2, l3, l4])

    checker = InclusionChecker(point, polygon)
    is_included = checker.point_inclusion()

    assert is_included
