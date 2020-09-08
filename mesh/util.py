"""Utility classes."""

from typing import List

import matplotlib.pyplot as plt

from mesh.primitives import Point, Line


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
