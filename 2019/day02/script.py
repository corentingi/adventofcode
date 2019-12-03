#!/usr/bin/env python3
# coding: utf8


import re


class ComputeException(Exception):
    pass


def _compute(program):
    _list = program

    # Pointer
    p = 0
    while True:
        opcode = _list[p]
        if opcode == 1:
            _list[_list[p + 3]] = (_list[_list[p + 1]]) + _list[_list[p + 2]]
        elif opcode == 2:
            _list[_list[p + 3]] = (_list[_list[p + 1]]) * _list[_list[p + 2]]
        elif opcode == 99:
            break
        else:
            raise ComputeException('Unknown opcode: {}'.format(opcode))

        p += 4

    return _list


def intcode_computer_part1(input_data):
    lines = [int(e) for e in re.split(',', input_data.strip())]

    lines[1] = 12
    lines[2] = 2

    result = _compute(lines)

    return result[0]


def intcode_computer_part2(input_data):
    # Let's ignore the case where noun or verb == 99 as this is not possible
    for noun in range(0, 99):
        for verb in range(0, 99):
            lines = [int(e) for e in re.split(',', input_data.strip())]
            lines[1] = noun
            lines[2] = verb

            try:
                result = _compute(lines)
            except ComputeException:
                continue

            if result[0] == 19690720:
                return 100 * noun + verb

    raise Exception('No combination has been found')


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print('Part 1:', intcode_computer_part1(input_data))
    print('Part 2:', intcode_computer_part2(input_data))
