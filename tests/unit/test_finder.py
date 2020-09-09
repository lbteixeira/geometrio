"""Module to test the algorithms to find intersections between lines."""

from mesh.finder import IntersectionFinder
from mesh.util import ProblemSetup


def test_brute_force():
    """Test the brute force method to find intersections."""

    ps = ProblemSetup("..\\mesh\\tests\\data\\input_points.txt")
    finder = IntersectionFinder(ps.create_lines())
    result = finder.brute_force()

    expected = 1

    assert result == expected
