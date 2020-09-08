"""Module to implement the main data structures of the problem: events queue and
status.
"""

from sortedcontainers import SortedList


class Status:
    """Class to represent the sweep line status."""

    status_line: SortedList
