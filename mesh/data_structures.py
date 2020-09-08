"""Module to implement the main data structures of the problem: events queue and
status.
"""

from typing import List

from sortedcontainers import SortedList

from mesh.line import Line
from mesh.events import EventsFactory as ef


class EventQueue:
    """Class to represent the events queue. The main data structure is a sorted
    list.
    """

    event_queue: SortedList

    def __init__(self, lines_list: List[Line]):

        self.event_queue = SortedList()
        for line in lines_list:
            if line.point1 < line.point2:
                p1, p2 = "EndPoint", "StartPoint"
            else:
                p1, p2 = "StartPoint", "EndPoint"

            self.event_queue.add(ef.create_event(p1, line.point1))
            self.event_queue.add(ef.create_event(p2, line.point2))
