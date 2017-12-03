#!/usr/bin/env python3
# coding: utf8

import re


def checksum(spreadsheet):
    result = 0

    lines = re.split('\n', spreadsheet.strip())

    for line in lines:
        values = list(map(int, re.split('\s+', line)))
        result += max(values) - min(values)

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print(checksum(input_data))
