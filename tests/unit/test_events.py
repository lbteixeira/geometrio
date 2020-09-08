"""Module to test the events operations."""

from mesh.events import EventQueue
from mesh.primitives import Line, Point

from mesh.events import StartPoint, EndPoint

def test_create_event_queue():
    """Tests if the event queue is created correctly, with all events in their
    expected position"""

    line1 = Line(Point(91, 179), Point(760, 353))
    line2 = Line(Point(874, 890), Point(648, 114))

    events = EventQueue([line1, line2])

    expected_points = [Point(648, 114), Point(91, 179), \
                       Point(760, 353), Point(874, 890)]

    point1 = events.event_queue._getitem(0).point
    point2 = events.event_queue._getitem(1).point
    point3 = events.event_queue._getitem(2).point
    point4 = events.event_queue._getitem(3).point
    result_points = [point1, point2, point3, point4]

    assert isinstance(events.event_queue._getitem(0), EndPoint)
    assert isinstance(events.event_queue._getitem(1), EndPoint)
    assert isinstance(events.event_queue._getitem(2), StartPoint)
    assert isinstance(events.event_queue._getitem(3), StartPoint)
    assert result_points == expected_points
