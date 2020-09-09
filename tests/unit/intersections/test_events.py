"""Module to test the events operations.

TODO: Test add_line_to_status with computation errors
"""


from sortedcontainers import SortedList

from geometrio.intersections.events import EventsQueue
from geometrio.intersections.primitives import Line, Point

from geometrio.intersections.events import StartPoint, EndPoint
from geometrio.intersections.events import EventsOperations as eo

def test_create_event_queue():
    """Tests if the event queue is created correctly, with all events in their
    expected position"""

    line1 = Line(Point(91, 179), Point(760, 353))
    line2 = Line(Point(874, 890), Point(648, 114))

    events = EventsQueue([line1, line2])

    expected_points = [Point(648, 114), Point(91, 179), \
                       Point(760, 353), Point(874, 890)]

    point1 = events.queue._getitem(0).point
    point2 = events.queue._getitem(1).point
    point3 = events.queue._getitem(2).point
    point4 = events.queue._getitem(3).point
    result_points = [point1, point2, point3, point4]

    assert isinstance(events.queue._getitem(0), EndPoint)
    assert isinstance(events.queue._getitem(1), EndPoint)
    assert isinstance(events.queue._getitem(2), StartPoint)
    assert isinstance(events.queue._getitem(3), StartPoint)
    assert result_points == expected_points


def test_add_line_to_status():

    status = SortedList()

    line1 = Line(Point(91, 179), Point(760, 353))
    line2 = Line(Point(874, 890), Point(648, 114))
    line3 = Line(Point(91, 179), Point(760, 353))
    line4 = Line(Point(91,179), Point(760, 353))
    line5 = Line(Point(91.3,179.7), Point(760.645, 353.15446))
    line6 = Line(Point(91.3,179.7), Point(760.645, 353.15446))

    eo.add_line_to_status(line1, status)
    eo.add_line_to_status(line2, status)
    eo.add_line_to_status(line3, status)
    eo.add_line_to_status(line4, status)
    eo.add_line_to_status(line5, status)
    eo.add_line_to_status(line6, status)

    assert len(status) == 3
