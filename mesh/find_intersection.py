"""Module to implement algorithms to find the number of intersections, given a
set of lines."""

from typing import List

from mesh.line import Line, ProblemSetup

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

if __name__ == "__main__":
    ps = ProblemSetup()
    input_list = ps.read_input_file("..\\mesh\\tests\\data\\input_points.txt")
    lines_list = ps.create_lines(input_list)
    ps.plot_input_lines(lines_list)

    intersections = brute_force(lines_list)
    print("Intersections: ", intersections)
