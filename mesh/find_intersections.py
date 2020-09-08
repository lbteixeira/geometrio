"""Module to implement algorithms to find the number of intersections, given a
set of lines."""

from typing import List

from mesh.primitives import Line
from mesh.events import EventsQueue


def brute_force(lines_list: List[Line]) -> int:
    """Brute force method. Verifies all line pairs.

    Parameters
    ----------
    lines_list : List[Line]
        List of lines.

    Returns
    -------
    number_of_intersections : int
    """

    number_of_intersections = 0
    for line1 in lines_list:
        for line2 in lines_list:
            if line1.do_intersect(line2) and line1 != line2:
                number_of_intersections += 1

    return int(number_of_intersections / 2)

def line_sweep(lines_list: List[Line]):

    events = EventsQueue(lines_list)

    while events.queue:
        new_event = events.queue.pop()
        new_event.handle_event()
