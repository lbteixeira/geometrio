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

    result = [line1._compute_orientation(point1),
              line1._compute_orientation(point2),
              line1._compute_orientation(point3)]

    expected = [-1, 1, 0]

    assert result == expected
