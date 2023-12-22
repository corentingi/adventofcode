from script import challenge_part1, challenge_part2


TEST_INPUT = """\
Time:      7  15   30
Distance:  9  40  200
"""

def test_challenge_part1():
    input_data = TEST_INPUT.splitlines()
    assert challenge_part1(input_data) == 288, "Do not pass"

def test_challenge_part2():
    input_data = TEST_INPUT.splitlines()
    assert challenge_part2(input_data) == 71503, "Do not pass"


if __name__ == "__main__":
    test_challenge_part1()
    test_challenge_part2()
