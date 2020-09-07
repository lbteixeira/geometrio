"""Module to implement the events and the events factory."""


from abc import abstractmethod

from mesh.line import Point


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

    def __init__(self, point: Point):
        self.point = point

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

    def handle_event(self):
        pass
