#!/usr/bin/env python3
# coding: utf8

import unittest
from script import manhattan_steps

cases = [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
]


class TestScript(unittest.TestCase):

    def test_manhattan_steps(self):
        for input_value, expected in cases:
            result = manhattan_steps(input_value)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
