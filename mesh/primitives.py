"""Module defining prilitives operations (lines and points)."""


class Point:
    """Class representing a point in the x-y space."""

    coord_x: float
    coord_y: float
    point_id: int
    point_count: int = 0

    def __init__(self, x: float, y: float):
        self.coord_x = x
        self.coord_y = y
        self.point_id = Point.point_count + 1
        Point.point_count += 1

    def __eq__(self, other_point, tol: float = 10**(-6)) -> bool:

        x_is_equal = self._is_equal(self.coord_x, other_point.coord_x, tol)
        y_is_equal = self._is_equal(self.coord_y, other_point.coord_y, tol)

        return x_is_equal and y_is_equal

    @staticmethod
    def _is_equal(value1: float, value2: float, tol: float):
        """Chacks if two values are equal within a given tolerance.

        Parameters
        ----------
        value1 : float
        value2 : float
        tol : float
            Tolerance
        """

        if value1 == 0:
            is_equal = abs((value1 - value2)) < tol
        else:
            is_equal = abs((value1 - value2)) /  value1 < tol * value1

        return is_equal

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
    line_id: int
    line_count: int = 0

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.line_id = Line.line_count + 1
        Line.line_count += 1

    def __eq__(self, other_line):
        return self.point1 == other_line.point1 and \
               self.point2 == other_line.point2

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
