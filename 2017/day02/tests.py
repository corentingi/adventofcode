#!/usr/bin/env python3
# coding: utf8

import unittest
from script import checksum_part1, checksum_part2

sample_part1 = """
5 1 9 5
7 5 3
2 4 6 8
"""
expected_result_part1 = 18

sample_part2 = """
5 9 2 8
9 4 7 3
3 8 6 5
"""
expected_result_part2 = 9


class TestScript(unittest.TestCase):

    def test_checksum_part1(self):
        result = checksum_part1(sample_part1)
        self.assertEqual(result, expected_result_part1)

    def test_checksum_part2(self):
        result = checksum_part2(sample_part2)
        self.assertEqual(result, expected_result_part2)


if __name__ == '__main__':
    unittest.main()
