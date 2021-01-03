"""Module to test the functionalities of the primitives."""


from geometrio.primitives.primitives import Line, Point


def test_is_at_right():
    """Tests the function is_at_right"""
    point1 = Point(3.0, 1.0)
    point2 = Point(0.7, 1.42)
    point3 = Point(0.25, -0.31)
    point4 = Point(1.97, -0.68)
    point5 = Point(1.77, 2.82)
    point6 = Point(4.28, 2.6)
    point7 = Point(1.32, 0.1)
    point8 = Point(2.7, 2.01)

    assert point1.is_at_right(Line(point7, point8))
    assert not point2.is_at_right(Line(point7, point8))
    assert not point3.is_at_right(Line(point7, point8))
    assert point4.is_at_right(Line(point7, point8))
    assert not point5.is_at_right(Line(point7, point8))
    assert point6.is_at_right(Line(point7, point8))


def test_get_intersection_point():
    """Tests the function get_intersection_point."""

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 1), Point(1, 0))
    line3 = Line(Point(0, 1), Point(1, 1))
    line4 = Line(Point(0, 0), Point(0, 1))
    line5 = Line(Point(-1, 0), Point(1, 0))

    expected = [Point(0.5, 0.5), Point(1, 1), Point(0, 0)]
    result = [line1.get_intersection_point(line2),
              line1.get_intersection_point(line3),
              line4.get_intersection_point(line5)]

    assert result == expected


def test_point_equal():
    """Tests if the equality operator was correctly overriden."""

    p1 = Point(1, 1)
    p2 = Point(1, 1)
    p3 = Point(0, 1)
    p4 = Point(1, 0)

    p5 = Point(1.000001, 0)
    p6 = Point(1.00001, 0)

    assert p1 == p2
    assert p1 != p3
    assert p1 != p4
    assert p4 == p5
    assert p4 != p6


def test_point_smaller():
    """Tests if the lower than operator was correctly overriden."""

    p1 = Point(1, 1)
    p2 = Point(0.5, 1)
    p3 = Point(0, 5)
    p4 = Point(1, 0)

    result = [p1 < p2, p1 < p3, p1 < p4]
    expected = [True, True, False]

    assert result == expected


def test_compute_orientation():
    """Test the method _compute_orientation."""

    line1 = Line(Point(0, 0), Point(1, 1))

    point1 = Point(0.5, 3)
    point2 = Point(0.5, -3)
    point3 = Point(0.5, 0.5)

    result = [line1.compute_orientation(point1),
              line1.compute_orientation(point2),
              line1.compute_orientation(point3)]

    expected = [-1, 1, 0]

    assert result == expected


def test_do_intersect():
    """Test the method do_intersect."""

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 1), Point(1, 0))
    line3 = Line(Point(2, 2), Point(3, 0))
    line4 = Line(Point(0, 1), Point(0, 0))
    line5 = Line(Point(-0.5, 0.5), Point(0.5, 0.5))
    line6 = Line(Point(-0.5, -0.5), Point(0.5, -0.5))
    line7 = Line(Point(0, 0), Point(1, 0))

    result_1 = line1.do_intersect(line2)
    result_2 = line1.do_intersect(line3)
    result_3 = line4.do_intersect(line5)
    result_4 = line4.do_intersect(line6)
    result_5 = line4.do_intersect(line7)

    assert result_1
    assert not result_2
    assert result_3
    assert not result_4
    assert result_5


def test_line_counting():
    """Tests if the class variable to count the lines is updated."""

    Line.line_count = 0

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 1), Point(1, 0))
    line3 = Line(Point(2, 2), Point(3, 0))

    assert line1.line_id == 1
    assert line2.line_id == 2
    assert line3.line_id == 3
    assert Line.line_count == 3


def test_line_equal():
    """Tests the method to check if two lines are equal."""

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 1), Point(1, 0))
    line3 = Line(Point(0, 0), Point(1, 1))

    assert line1 != line2
    assert line1 == line3


def test_line_smaller():
    """Tests if __lt__ was correctly overrided."""

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 1), Point(1, 0))
    line3 = Line(Point(0, 0), Point(1, -1))

    assert line2 > line1
    assert line1 > line3
    assert line3 < line2
