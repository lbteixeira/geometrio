"""Module defining line operations."""

from typing import Tuple
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


if __name__ == "__main__":
    line1 = Line((0, 0), (1, 1))
    line2 = Line((0, 5), (1, 1))
    ptr = LinePlotter()
    ptr.plot_line(line1)
    ptr.plot_line(line2)
    ptr.show_plot()
