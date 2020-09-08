"""Module to implement the main data structures of the problem: events queue and
status.
"""

from sortedcontainers import SortedList

from mesh.line import Line, Point
from mesh.events import EventsFactory as ef


class EventQueue:
    """Class to represent the events queue. The main data structure is a sorted
    list.
    """

    event_queue: SortedList

    def __init__(self, lines_list: Line):

        event_queue = SortedList()
        for line in lines_list:
            event_queue.add(ef.create_event("StartPoint", line.point1))
            event_queue.add(ef.create_event("EndPoint", line.point2))


if __name__ == "__main__":
    eq = EventQueue([Line(Point(1, 1), Point(0, 0))])
    y = 1
