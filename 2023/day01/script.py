from pathlib import Path


numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def trebuchet_part1(input_data):
    _sum = 0

    for line in input_data:
        digits = list(filter(lambda c: c.isdigit(), line))
        parameter = int(digits[0] + digits[-1])
        _sum += parameter

    return _sum


def trebuchet_part2(input_data):
    _sum = 0

    for line in input_data:
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(line[i])
                continue
            for number in numbers:
                if line[i:].startswith(number):
                    digits.append(numbers[number])
                    break

        parameter = int(digits[0] + digits[-1])
        _sum += parameter

    return _sum



if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        input_data = list(map(lambda s: s.strip(), f.readlines()))

    print("Part 1:", trebuchet_part1(input_data))
    print("Part 2:", trebuchet_part2(input_data))
