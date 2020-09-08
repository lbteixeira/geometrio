"""Module to test the algorithms to find intersections between lines."""

from mesh.find_intersections import brute_force
from mesh.line import ProblemSetup


def test_brute_force():
    """Test the brute force method to find intersections."""

    ps = ProblemSetup()
    input_list = ps.read_input_file("..\\mesh\\tests\\data\\input_points.txt")
    lines_list = ps.create_lines(input_list)

    expected = 1
    result = brute_force(lines_list)

    assert result == expected
