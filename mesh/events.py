"""Module to implement the events and the events factory."""


class EventsFactory():
    """Concrete creator for events objects."""

    @staticmethod
    def create_event(event_type: str):
        """Factory method for event objects.

        Parameters
        ----------
        event_type : str
            Type of event.
        """

        try:
            if event_type == "StartPoint":
                return StartPoint()
            elif event_type == "EndPoint":
                return EndPoint()
            elif event_type == "Intersection":
                return Intersection()
            raise AssertionError("Event type not found")
        except AssertionError as _error:
            print(_error)
