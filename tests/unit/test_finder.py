"""Module to test the algorithms to find intersections between lines."""

from geometrio.finder import IntersectionFinder
from geometrio.util import ProblemSetup


def test_brute_force():
    """Test the brute force method to find intersections."""

    ps = ProblemSetup("..\\geometrio\\tests\\data\\input_points.txt")
    finder = IntersectionFinder(ps.create_lines())
    result = finder.brute_force()

    expected = 1

    assert result == expected
