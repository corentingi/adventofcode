import logging
from pathlib import Path
import re
from functools import reduce


MATCH_NUMBERS = re.compile(r"[0-9]+")
MATCH_SPECIAL_CHARACTERS = re.compile(r"[^.0-9]+")
MATCH_ASTERSIK = re.compile(r"\*")


def challenge_part1(input_data):
    numbers_to_sum = []
    for i in range(len(input_data)):
        current_line = input_data[i]
        previous_line = input_data[i - 1] if i > 0 else '.' * len(current_line)
        next_line = input_data[i + 1] if i < len(input_data) - 1 else '.' * len(current_line)

        for m in MATCH_NUMBERS.finditer(current_line):
            _start = max(0, m.start() - 1)
            _end = min(len(current_line) - 1, m.end() + 1)
            around_chars = (
                previous_line[_start:_end] +
                next_line[_start:_end] +
                current_line[_start:m.start()] +
                current_line[m.end():_end]
            )

            if MATCH_SPECIAL_CHARACTERS.search(around_chars):
                numbers_to_sum.append(int(m.group()))
                logging.debug("There is a special char around")
            else:
                logging.debug("No special char around")
    return sum(numbers_to_sum)


def challenge_part2(input_data):
    numbers_to_sum = []

    line_numbers = {}
    for i, line in enumerate(input_data):
        line_numbers[i] = list(MATCH_NUMBERS.finditer(line))

    for i in range(len(input_data)):
        current_line = input_data[i]

        numbers = list(line_numbers[i])
        if i > 0:
            numbers += line_numbers[i - 1]
        if i < len(input_data) - 1:
            numbers += line_numbers[i + 1]

        for m in MATCH_ASTERSIK.finditer(current_line):
            _start = max(0, m.start() - 1)
            _end = min(len(current_line) - 1, m.end() + 1)

            gear_ratios = []
            for number in numbers:
                if (_start <= number.start() < _end) or (_start < number.end() <= _end):
                    logging.debug("Number is adjacent: %s" % number.group())
                    gear_ratios.append(int(number.group()))

            if len(gear_ratios) == 2:
                numbers_to_sum.append(gear_ratios[0] * gear_ratios[1])

    return sum(numbers_to_sum)



if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        input_data = list(map(lambda s: s.strip(), f.readlines()))

    print("Part 1:", challenge_part1(input_data))
    print("Part 2:", challenge_part2(input_data))
