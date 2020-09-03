from mesh.line import ProblemSetup


def test_read_input_file():
    input_file = "..\\mesh\\tests\\data\\input_points.txt"
    expected = [[91, 179, 760, 353], [874, 890, 648, 114]]

    ps = ProblemSetup()
    result = ps.read_input_file(input_file)

    assert result == expected
