from functools import reduce
import math
import operator
from pathlib import Path
import re


NUMBER_PATTERN = re.compile(r"[0-9]+")

def second_degree_roots(a, b, c):
    """
    Return the roots of a*x^2 + b*x + c
    """
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return (
            (-b + math.sqrt(discriminant)) / (2*a),
            (-b - math.sqrt(discriminant)) / (2*a),
        )
    elif discriminant == 0:
        return (
            (-b / (2*a)),
            (-b / (2*a)),
        )
    else:
        raise Exception("No solution in the real numbers")


def challenge_part1(input_data):
    """
    Here the problem can be solved as follows:
        - T is the time of the race
        - D is the distance to win the race
        We need to find the number of integer values between the roots of
        f(x) = -x^2 + T*x - D
    """
    times = list(map(int, NUMBER_PATTERN.findall(input_data[0])))
    distances = list(map(int, NUMBER_PATTERN.findall(input_data[1])))

    ways = []
    for time, distance in zip(times, distances):
        roots = second_degree_roots(-1, time, -distance)
        int_roots = math.floor(roots[0]) + 1, math.ceil(roots[1]) - 1
        ways.append(len(range(int_roots[0], int_roots[1] + 1)))

    return reduce(operator.mul, ways)


def challenge_part2(input_data):
    """
    Here the problem can be solved as follows:
        - T is the time of the race
        - D is the distance to win the race
        We need to find the number of integer values between the roots of
        f(x) = -x^2 + T*x - D
    """
    time = int("".join(NUMBER_PATTERN.findall(input_data[0])))
    distance = int("".join(NUMBER_PATTERN.findall(input_data[1])))

    roots = second_degree_roots(-1, time, -distance)
    int_roots = math.floor(roots[0]) + 1, math.ceil(roots[1]) - 1
    return len(range(int_roots[0], int_roots[1] + 1))


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        input_data = list(map(lambda s: s.strip(), f.readlines()))

    print("Part 1:", challenge_part1(input_data))
    print("Part 2:", challenge_part2(input_data))
