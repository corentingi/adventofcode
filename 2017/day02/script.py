#!/usr/bin/env python3
# coding: utf8

import re


def checksum_part1(spreadsheet):
    result = 0

    lines = re.split('\n', spreadsheet.strip())

    for line in lines:
        values = list(map(int, re.split('\s+', line)))
        result += max(values) - min(values)

    return result


def checksum_part2(spreadsheet):
    result = 0

    lines = re.split('\n', spreadsheet.strip())

    for line in lines:
        values = list(map(int, re.split('\s+', line)))
        values.sort(reverse=True)
        n = len(values)

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if values[i] % values[j] == 0:
                    result += int(values[i] / values[j])

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print('Part 1:', checksum_part1(input_data))
    print('Part 2:', checksum_part2(input_data))
