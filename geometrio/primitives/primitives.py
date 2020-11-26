"""Module defining primitive objects (lines and points)."""
from math import isclose
from typing import List


class Point:
    """Class representing a point in the x-y space."""

    coord_x: float
    coord_y: float
    point_id: int
    point_count: int = 0
    which_line: int

    def __init__(self, x: float, y: float):
        Point.point_count += 1
        self.coord_x = x
        self.coord_y = y
        self.point_id = Point.point_count

    def __eq__(self, other_point, tol: float = 10 ** (-6)) -> bool:

        x_is_equal = isclose(self.coord_x, other_point.coord_x, rel_tol=tol)
        y_is_equal = isclose(self.coord_y, other_point.coord_y, rel_tol=tol)

        return x_is_equal and y_is_equal

    def __lt__(self, other_point) -> bool:
        """Overrides the lower than operator.

        Condition:
            1. One point will be lower than the other if its y coordinate is
        lower
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

        is_smaller = False
        if self.coord_y < other_point.coord_y:
            is_smaller = True
        elif isclose(self.coord_y, other_point.coord_y, rel_tol=10 ** (-6)) \
                and self.coord_x > other_point.coord_x:
            is_smaller = True

        return is_smaller

    def is_at_right(self, line) -> bool:
        """Check if the point is at the right of a line"""
        ordered_points = line.order_points()
        a = ordered_points[0]
        b = ordered_points[1]

        if a.coord_y < self.coord_y and b.coord_y > self.coord_y and \
           self.makes_right_turn(a, b):
            return True
        else:
            return False

    def makes_right_turn(self, point_a, point_b) -> bool:
        """Checks if the points abc make a right turn

        c is the current point.
        """
        ax, ay = point_a.coord_x, point_a.coord_y
        bx, by = point_b.coord_x, point_b.coord_y
        cx, cy = self.coord_x, self.coord_y

        area = (bx - ax)*(cy - ay) - (cx - ax)*(by - ay)

        makes_right_turn = False
        if area < 0:
            makes_right_turn = True

        return makes_right_turn


class Line:

    """Class representing a line segment."""

    point1: Point
    point2: Point
    line_id: int
    line_count: int = 0

    def __init__(self, point1: Point, point2: Point):
        Line.line_count += 1
        self.point1 = point1
        self.point2 = point2
        self.line_id = Line.line_count

    def __eq__(self, other_line) -> bool:
        return self.point1 == other_line.point1 and \
            self.point2 == other_line.point2

    def __lt__(self, other_line) -> bool:
        ordered_self = self.order_points()
        ordered_other = other_line.order_points()

        if ordered_self[1] < ordered_other[1]:
            return True
        else:
            return False

    def order_points(self) -> List[Point]:
        """Order the points of the line"""

        if self.point1 < self.point2:
            return [self.point1, self.point2]
        else:
            return [self.point2, self.point1]

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

        x = ((x1 * y2 - y1 * x2) * (x3 - x4) -
             (x1 - x2) * (x3 * y4 - y3 * x4)) / \
            ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        y = ((x1 * y2 - y1 * x2) * (y3 - y4) -
             (y1 - y2) * (x3 * y4 - y3 * x4)) / \
            ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

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


class Polygon():
    """Class representing a polygon.

    A polygon is a list of lines.
    """

    lines: List[Line]

    def __init__(self, lines: List[Line]):
        self.lines = lines


if __name__ == "__main__":
    p = Point(1, 2)
    a = p.coord_x
