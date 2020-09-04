"""Module defining line operations."""


from typing import Tuple, List

import matplotlib.pyplot as plt

class Line:
    """Class representing a line segment."""

    point1: Tuple
    point2: Tuple

    def __init__(self, point1: Tuple, point2: Tuple):
        self.point1 = point1
        self.point2 = point2

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
        else:
            intersection = False

        return intersection

    def compute_orientation(self, point: Tuple) -> int:
        """Computes the orientation between two segments.

        The two segments are formed between a line (first segment) and a point.

        1 -> Clockwise
        -1 -> Counterclockwise
        0 -> colinear

        Parameters
        ----------
        point : Tuple
            A point in the space.

        Returns
        -------
        orientation : int
            Orientation of the segments.
        """

        x1, y1 = self.point1
        x2, y2 = self.point2
        x3, y3 = point

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

    def plot_line(self, line: Line):
        """Plots a line in the figure.

        Parameters
        ----------
        line : Line
            Line to be plotted
        """
        x1, y1 = line.point1
        x2, y2 = line.point2

        self.axes.plot([x1, x2], [y1, y2])

    def show_plot(self):
        """Convenience method to show the plots"""
        plt.show()


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
            new_line = Line((coords[0], coords[1]), (coords[2], coords[3]))
            lines_list.append(new_line)

        return lines_list


    @staticmethod
    def plot_input_lines(lines_list: List[Line]):
        """Plots the lines for visual inspection of the problem domain.

        Parameters
        ----------
        lines_list : List[Line]
            List of lines to be plotted.
        """

        plr = LinePlotter()
        for line in lines_list:
            plr.plot_line(line)

        plr.show_plot()


if __name__ == "__main__":
    ps = ProblemSetup()
    input_list = ps.read_input_file("..\\mesh\\tests\\data\\input_points.txt")
    lines_list = ps.create_lines(input_list)
    ps.plot_input_lines(lines_list)
