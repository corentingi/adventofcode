#!/usr/bin/env python3
# coding: utf8

import unittest
from script import manhattan_steps_part1, manhattan_steps_part2

cases_part1 = [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
]


class TestScript(unittest.TestCase):

    def test_manhattan_steps_part1(self):
        for input_value, expected in cases_part1:
            result = manhattan_steps_part1(input_value)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
