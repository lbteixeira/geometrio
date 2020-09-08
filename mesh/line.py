"""Module defining line operations."""


from typing import List

import matplotlib.pyplot as plt


class Point:
    """Class representing a point in the x-y space."""

    coord_x: float
    coord_y: float

    def __init__(self, x: float, y: float):
        self.coord_x = x
        self.coord_y = y

    def __eq__(self, other_point) -> bool:
        x = self.coord_x == other_point.coord_x
        y = self.coord_y == other_point.coord_y

        return x and y

    def __lt__(self, other_point) -> bool:
        """Overrides the lower than operator.

        Condition:
            1. One point will be lower than the other if its y coordinate is lower
            2. If the y coordinates are the same, the one with the smaller x
            coordinate will be smaller

        Parameters
        ----------
        other_point : Point
            Point to be compared with the current point.

        Returns
        -------
        is_smaller : bool
            True if the current point is smaller, False otherwise.
        """

        if self.coord_y < other_point.coord_y:
            is_smaller = True
        elif self.coord_y == other_point.coord_y and \
             self.coord_x > other_point.coord_x:
            is_smaller = True
        else:
            is_smaller = False

        return is_smaller


class Line:
    """Class representing a line segment."""

    point1: Point
    point2: Point

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def __eq__(self, other_line) -> bool:
        """Overrides the equality operator.

        Two lines are said to be equal if and only if all coordinates of both
        points are the same.

        Parameters
        ----------
        other_line : Line
            Line to be compared with the current line.

        Returns
        -------
        True if the coordinates are the same, False otherwise.
        """

        p1 = self.point1 == other_line.point1
        p2 = self.point2 == other_line.point2

        return p1 and p2

    def get_intersection_point(self, other_line) -> Point:
        """Calculates the intersection point between two lines.

        Parameters
        ----------
        other_line : Line

        Returns
        -------
        Point
            Point where the lines intersect
        """

        x1, y1 = self.point1.coord_x, self.point1.coord_y
        x2, y2 = self.point2.coord_x, self.point2.coord_y
        x3, y3 = other_line.point1.coord_x, other_line.point1.coord_y
        x4, y4 = other_line.point2.coord_x, other_line.point2.coord_y

        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) \
            / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) \
            / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        return Point(x, y)

    def do_intersect(self, other_line) -> bool:
        """Verifies if the current line segment intersects another line.

        Parameters
        ----------
        other_line : Line
            Line to have the intersection checked.

        Returns
        -------
        intersection : bool
            True if the lines intersect, False if they don't.
        """

        orien_1 = self.compute_orientation(other_line.point1)
        orien_2 = self.compute_orientation(other_line.point2)
        orien_3 = other_line.compute_orientation(self.point1)
        orien_4 = other_line.compute_orientation(self.point2)

        if (orien_1 * orien_2) < 0 and (orien_3 * orien_4) < 0:
            intersection = True
        elif (orien_1 * orien_2) == 0 and (orien_3 * orien_4) == 0:
            intersection = True
        else:
            intersection = False

        return intersection

    def compute_orientation(self, point: Point) -> int:
        """Computes the orientation between two segments.

        The two segments are formed between a line (first segment) and a point.

        1 -> Clockwise
        -1 -> Counterclockwise
        0 -> colinear

        Parameters
        ----------
        point : Point
            A point in the space.

        Returns
        -------
        orientation : int
            Orientation of the segments.
        """

        x1, y1 = self.point1.coord_x, self.point1.coord_y
        x2, y2 = self.point2.coord_x, self.point2.coord_y
        x3, y3 = point.coord_x, point.coord_y

        expression = (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)

        if expression > 0:
            orientation = 1
        elif expression < 0:
            orientation = -1
        else:
            orientation = 0

        return orientation


class LinePlotter:
    """Creates a figure environment, customizes it and plots the lines."""

    def __init__(self):
        self.fig = plt.figure()
        self.axes = plt.axes()

    def plot_input_lines(self, lines_list: List[Line]):
        """Plots the lines for visual inspection of the problem domain.

        Parameters
        ----------
        lines_list : List[Line]
            List of lines to be plotted.
        """

        for line in lines_list:
            self.plot_line(line)

        plt.show()

    def plot_line(self, line: Line):
        """Plots a line in the figure.

        Parameters
        ----------
        line : Line
            Line to be plotted
        """
        x1, y1 = line.point1.coord_x, line.point1.coord_y
        x2, y2 = line.point2.coord_x, line.point2.coord_y

        self.axes.plot([x1, x2], [y1, y2])


class ProblemSetup():
    """Class to pre-process the input data."""

    @staticmethod
    def read_input_file(input_file) -> List[float]:
        """Reads the input file containing the points coordinates.

        Parameters
        ----------
        input_file : .txt
            File to be read.

        Returns
        -------
        input_list : List[float]
            List with the coordinates of the points.
        """

        input_list = []
        with open(input_file, "r") as f:
            for line in f:
                coords = [int(x) for x in line.split()]
                input_list.append(coords)

        return input_list

    @staticmethod
    def create_lines(input_list: List[float]) -> List[Line]:
        """Creates the lines based on the input file.

        Parameters
        ----------
        input_list : List[float]
            List with the coordinates of the points.
        Returns
        -------
        lines: List[Line]
            List of the created lines.
        """

        lines_list = []
        for coords in input_list:
            new_line = Line(Point(coords[0], coords[1]), Point(coords[2], coords[3]))
            lines_list.append(new_line)

        return lines_list
