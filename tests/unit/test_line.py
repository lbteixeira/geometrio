from mesh.line import ProblemSetup, Line


def test_read_input_file():
    """Test the method read_input_file."""

    input_file = "..\\mesh\\tests\\data\\input_points.txt"
    expected = [[91, 179, 760, 353], [874, 890, 648, 114]]

    ps = ProblemSetup()
    result = ps.read_input_file(input_file)

    assert result == expected

def test_create_lines():
    """Test the method create_lines."""

    input_list = [[91, 179, 760, 353], [874, 890, 648, 114]]
    line1 = Line((91, 179), (760, 353))
    line2 = Line((874, 890), (648, 114))
    ps = ProblemSetup()

    expected = [line1, line2]
    result = ps.create_lines(input_list)

    for res, exp in zip(result, expected):
        assert res.point1 == exp.point1
        assert res.point2 == exp.point2

def test_compute_orientation():
    """Test the method _compute_orientation."""

def test_compute_line_slope():
    """Test the method _compute_line_slope."""
    
    point1 = (0, 0)
    point2 = (1, 1)
    line = Line(point1, point2)

    expected = 1
    result = line._compute_line_slope()
    assert result == expected
