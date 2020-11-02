"""Module to implement algorithms to find the number of intersections, given a
set of lines."""

from typing import List
from abc import abstractmethod

from geometrio.primitives.primitives import Line
from geometrio.intersections.events import EventsQueue


class IntersectionFinder():
    """Class containing methods to find intersections between sets of lines."""

    lines_list: List[Line]

    def __init__(self, lines_list: List[Line]):
        self.lines_list = lines_list

    @abstractmethod
    def initialize(self):
        """Initializes the problem."""

    @abstractmethod
    def execute(self) -> int:
        """Executes the intersection finding job.

        Returns
        -------
        number_of_intersections : int
        """


class BruteForce(IntersectionFinder):
    """Brute force method (naive). Verifies all line pairs."""

    def initialize(self) -> int:
        """This calculation method is initialized upon the call to __init__"""

    def execute(self) -> int:

        number_of_intersections = 0
        for line1 in self.lines_list:
            for line2 in self.lines_list:
                if line1.do_intersect(line2) and line1 != line2:
                    number_of_intersections += 1

        return int(number_of_intersections / 2)


class LineSweep(IntersectionFinder):
    """Line sweep method."""

    events: EventsQueue

    def initialize(self):

        self.events = EventsQueue(self.lines_list)

    def execute(self):

        while self.events.queue:
            new_event = self.events.queue.pop()
            new_event.handle_event()
