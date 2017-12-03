#!/usr/bin/env python3
# coding: utf8

import unittest
from script import checksum

sample = """
5 1 9 5
7 5 3
2 4 6 8
"""
expected_result = 18


class TestSumCaptcha(unittest.TestCase):

    def test_sum_captcha(self):
        result = checksum(sample)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
