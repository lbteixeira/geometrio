"""Module to test the main data structures of the problem: events queue and
status.
"""

from mesh.data_structures import EventQueue
from mesh.line import Line, Point
from mesh.events import StartPoint, EndPoint

def test_create_event_queue():
    """Tests if the event queue is created correctly, with all events in their
    expected position"""

    line1 = Line(Point(91, 179), Point(760, 353))
    line2 = Line(Point(874, 890), Point(648, 114))

    eq = EventQueue([line1, line2])

    expected_points = [Point(648, 114), Point(91, 179), \
                       Point(760, 353), Point(874, 890)]

    p1 = eq.event_queue._getitem(0).point
    p2 = eq.event_queue._getitem(1).point
    p3 = eq.event_queue._getitem(2).point
    p4 = eq.event_queue._getitem(3).point
    result_points = [p1, p2, p3, p4]

    assert isinstance(eq.event_queue._getitem(0), EndPoint)
    assert isinstance(eq.event_queue._getitem(1), EndPoint)
    assert isinstance(eq.event_queue._getitem(2), StartPoint)
    assert isinstance(eq.event_queue._getitem(3), StartPoint)
    assert result_points == expected_points
