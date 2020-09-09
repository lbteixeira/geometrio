"""Module to test the algorithms to find intersections between lines."""

from mesh.finder import IntersectionFinder
from mesh.util import ProblemSetup


def test_brute_force():
    """Test the brute force method to find intersections."""

    ps = ProblemSetup()
    input_list = ps.read_input_file("..\\mesh\\tests\\data\\input_points.txt")
    lines_list = ps.create_lines(input_list)

    expected = 1
    finder = IntersectionFinder(lines_list)
    result = finder.brute_force()

    assert result == expected
