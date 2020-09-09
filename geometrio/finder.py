"""Module to implement algorithms to find the number of intersections, given a
set of lines."""

from typing import List

from geometrio.primitives import Line
from geometrio.events import EventsQueue


class IntersectionFinder():
    """Class containing methods to find intersections between sets of lines."""

    lines_list: List[Line]

    def __init__(self, lines_list: List[Line]):
        self.lines_list = lines_list

    def brute_force(self) -> int:
        """Brute force method (naive). Verifies all line pairs.

        Returns
        -------
        number_of_intersections : int
        """

        number_of_intersections = 0
        for line1 in self.lines_list:
            for line2 in self.lines_list:
                if line1.do_intersect(line2) and line1 != line2:
                    number_of_intersections += 1

        return int(number_of_intersections / 2)


    def line_sweep(self):
        """Line sweep method.

        Returns
        -------
        number_of_intersections : int
        """

        events = EventsQueue(self.lines_list)

        while events.queue:
            new_event = events.queue.pop()
            new_event.handle_event()
