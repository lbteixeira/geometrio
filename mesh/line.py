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
        coords_x = [line.point1[0], line.point2[0]]
        coords_y = [line.point1[1], line.point2[1]]
        self.axes.plot(coords_x, coords_y)

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
    pass
