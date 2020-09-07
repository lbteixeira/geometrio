"""Module to test the functionalities of a line."""

from mesh.line import ProblemSetup, Line, Point


def test_point_equal():
    """Tests if the equality operator was correctly overriden."""

    p1 = Point(1, 1)
    p2 = Point(1, 1)
    p3 = Point(0, 1)
    p4 = Point(1, 0)

    assert p1 == p2
    assert p1 != p3
    assert p1 != p4

def test_point_smaller():
    """Tests if the lower than operator was correctly overriden."""

    p1 = Point(1, 1)
    p2 = Point(0.5, 1)
    p3 = Point(0, 5)
    p4 = Point(1, 0)

    result = [p1 < p2, p1 < p3, p1 < p4]
    expected = [False, True, False]

    assert result == expected

def test_read_input_file():
    """Test the method read_input_file."""

    input_file = "..\\mesh\\tests\\data\\input_points.txt"
    expected = [[91, 179, 760, 353], [874, 890, 648, 114]]

    problem = ProblemSetup()
    result = problem.read_input_file(input_file)

    assert result == expected

def test_create_lines():
    """Test the method create_lines."""

    input_list = [[91, 179, 760, 353], [874, 890, 648, 114]]
    line1 = Line(Point(91, 179), Point(760, 353))
    line2 = Line(Point(874, 890), Point(648, 114))
    problem = ProblemSetup()

    expected = [line1, line2]
    result = problem.create_lines(input_list)

    for res, exp in zip(result, expected):
        assert res.point1 == exp.point1
        assert res.point2 == exp.point2

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

def test_line_equal():
    """Test if the equality operator was correctly overriden."""

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 0), Point(1, 1))
    line3 = Line(Point(0, 1), Point(1, 1))
    line4 = Line(Point(0, 15), Point(15, 0))

    assert line1 == line2
    assert line1 != line3
    assert line1 != line4

def test_get_point_highest_y():
    """Test the function _get_point_highest_y."""

    line2 = Line(Point(0, 1), Point(1, 0))
    line3 = Line(Point(0, 1), Point(1, 1))
    line4 = Line(Point(1, 1), Point(0, 1))
    line1 = Line(Point(0, 0), Point(1, 1))

    expected_1 = Point(1, 1)
    expected_2 = Point(0, 1)
    expected_3 = Point(0, 1)
    expected_4 = Point(0, 1)

    result_1 = line1._get_point_highest_y()
    result_2 = line2._get_point_highest_y()
    result_3 = line3._get_point_highest_y()
    result_4 = line4._get_point_highest_y()

    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3
    assert result_4 == expected_4

def test_line_smaller():
    """Test if the lower than operator was correctly overriden."""

    line1 = Line(Point(0, 0), Point(1, 1))
    line2 = Line(Point(0, 0), Point(1, 2))
    line3 = Line(Point(0, 1), Point(1, 1))
    line4 = Line(Point(0, 15), Point(15, 0))

    result = [line1 < line2, line1 < line3, line1 < line1, \
              line1 < line4, line3 < line4, line4 < line2]

    expected = [True, False, False, True, True, False]

    assert result == expected
