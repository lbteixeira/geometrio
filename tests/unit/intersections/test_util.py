"""Module to test the utility functions."""

from geometrio.intersections.util import ProblemSetup
from geometrio.intersections.primitives import Point, Line


def test_create_lines():
    """Test the method create_lines."""

    input_file = "..\\geometrio\\tests\\data\\input_points.txt"

    line1 = Line(Point(91, 179), Point(760, 353))
    line2 = Line(Point(874, 890), Point(648, 114))
    expected = [line1, line2]

    ps = ProblemSetup(input_file)
    result = ps.create_lines()

    assert result == expected
