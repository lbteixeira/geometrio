from mesh.line import ProblemSetup, Line


def test_read_input_file():
    input_file = "..\\mesh\\tests\\data\\input_points.txt"
    expected = [[91, 179, 760, 353], [874, 890, 648, 114]]

    ps = ProblemSetup()
    result = ps.read_input_file(input_file)

    assert result == expected

def test_create_lines():
    input_list = [[91, 179, 760, 353], [874, 890, 648, 114]]
    line1 = Line((91, 179), (760, 353))
    line2 = Line((874, 890), (648, 114))
    ps = ProblemSetup()

    expected = [line1, line2]
    result = ps.create_lines(input_list)

    for res, exp in zip(result, expected):
        assert res.point1 == exp.point1
        assert res.point2 == exp.point2
