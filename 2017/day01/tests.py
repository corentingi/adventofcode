#!/usr/bin/env python3
# coding: utf8

import unittest
from script import sum_captcha_part1, sum_captcha_part2

cases_part1 = [
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
]

cases_part2 = [
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
]


class TestScript(unittest.TestCase):

    def test_sum_captcha_part1(self):
        for input_value, expected in cases_part1:
            result = sum_captcha_part1(input_value)
            self.assertEqual(result, expected)

    def test_sum_captcha_part2(self):
        for input_value, expected in cases_part2:
            result = sum_captcha_part2(input_value)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
