"""Module to implement the events and the events factory."""

from typing import List
from abc import abstractmethod

from sortedcontainers import SortedList

from mesh.primitives import Point, Line


class EventsOperations():
    """Defines operations the events can use when they are handled."""

    @staticmethod
    def add_line_to_status(line: Line, status: SortedList):
        """Inserts line to the status, if it's not already there.

        Parameters
        ----------
        line : Line
        status : SortedList
        """
        if line not in status:
            status.add(line)

    @staticmethod
    def check_which_line(point: Point) -> int:
        """Checks to which line a point is part of.

        TODO: verify case where two lines share a point.

        Parameters
        ----------
        point : Point

        Returns
        -------
        line_id: int
        """

        if point.point_id % 2 != 0:
            line_id = (point.point_id + 1) / 2
        else:
            line_id = point.point_id / 2

        return line_id


class EventsFactory():
    """Concrete creator for events objects."""

    @staticmethod
    def create_event(event_type: str, point: Point):
        """Factory method for event objects.

        Parameters
        ----------
        event_type : str
            Type of event.

        point: Point
            Point to be added as an event.
        """

        try:
            if event_type == "StartPoint":
                return StartPoint(point)
            elif event_type == "EndPoint":
                return EndPoint(point)
            elif event_type == "Intersection":
                return Intersection(point)
            raise AssertionError("Event type not found")
        except AssertionError as _error:
            print(_error)


class Events():
    """Product interface for the events objects."""

    point: Point
    operation: EventsOperations

    def __init__(self, point: Point):
        self.point = point
        self.operation = EventsOperations()

    def __lt__(self, other_event):
        return self.point < other_event.point

    @abstractmethod
    def handle_event(self):
        """Handles the event according to its type."""


class StartPoint(Events):
    """StartPoint event type."""

    def handle_event(self):
        pass


class EndPoint(Events):
    """EndPoint event type."""

    def handle_event(self):
        pass


class Intersection(Events):
    """Intersection event type."""

    num_intersections: int = 0

    def handle_event(self):
        self.num_intersections += 1


class EventsQueue:
    """Class to represent the events queue. The main data structure is a sorted
    list.
    """

    queue: SortedList
    status: SortedList

    def __init__(self, lines_list: List[Line]):

        self.status = SortedList()

        self.queue = SortedList()
        for line in lines_list:
            if line.point1 < line.point2:
                point1, point2 = "EndPoint", "StartPoint"
            else:
                point1, point2 = "StartPoint", "EndPoint"

            event_1 = EventsFactory.create_event(point1, line.point1)
            event_2 = EventsFactory.create_event(point2, line.point2)

            self.queue.add(event_1)
            self.queue.add(event_2)
