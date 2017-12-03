#!/usr/bin/env python3
# coding: utf8

import unittest
from script import sum_captcha

cases = [
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
]


class TestSumCaptcha(unittest.TestCase):

    def test_sum_captcha(self):
        for input_value, expected in cases:
            result = sum_captcha(input_value)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
