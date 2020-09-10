"""Module to test the algorithms to find intersections between lines."""

from geometrio.intersections.finder import BruteForce
from geometrio.intersections.util import ProblemSetup


def test_brute_force():
    """Test the brute force method to find intersections."""

    ps = ProblemSetup("..\\geometrio\\tests\\data\\input_points.txt")
    finder = BruteForce(ps.create_lines())
    result = finder.execute()

    expected = 1

    assert result == expected
