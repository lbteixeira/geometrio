"""Module to test the functionalities of a line."""

from mesh.line import ProblemSetup, Line


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
    line1 = Line((91, 179), (760, 353))
    line2 = Line((874, 890), (648, 114))
    problem = ProblemSetup()

    expected = [line1, line2]
    result = problem.create_lines(input_list)

    for res, exp in zip(result, expected):
        assert res.point1 == exp.point1
        assert res.point2 == exp.point2

def test_compute_orientation():
    """Test the method _compute_orientation."""

    line1 = Line((0, 0), (1, 1))

    point1 = (0.5, 3)
    point2 = (0.5, -3)
    point3 = (0.5, 0.5)

    result = [line1.compute_orientation(point1),
              line1.compute_orientation(point2),
              line1.compute_orientation(point3)]

    expected = [-1, 1, 0]

    assert result == expected

def test_do_intersect():
    """Test the method do_intersect."""

    line1 = Line((0, 0), (1, 1))
    line2 = Line((0, 1), (1, 0))
    line3 = Line((2, 2), (3, 0))
    line4 = Line((0, 1), (0, 0))
    line5 = Line((-0.5, 0.5), (0.5, 0.5))
    line6 = Line((-0.5, -0.5), (0.5, -0.5))
    line7 = Line((0, 0), (1, 0))

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
