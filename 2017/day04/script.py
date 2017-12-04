#!/usr/bin/env python3
# coding: utf8

import re


def valid_passphrases_part1(passphrases):
    result = 0

    for line in re.split('\n', passphrases.strip()):
        words = list(re.split('\s+', line))
        unique_words = set(words)

        if len(words) == len(unique_words):
            result += 1

    return result


def valid_passphrases_part2(passphrases):
    result = 0

    for line in re.split('\n', passphrases.strip()):
        words = list(re.split('\s+', line))
        ordered_words = [''.join(sorted(w)) for w in words]
        unique_words = set(ordered_words)

        if len(ordered_words) == len(unique_words):
            result += 1

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print('Part 1:', valid_passphrases_part1(input_data))
    print('Part 2:', valid_passphrases_part2(input_data))
