#!/usr/bin/env python3
# coding: utf8

import unittest
from script import valid_passphrases_part1, valid_passphrases_part2

sample_part1 = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
"""

expected_part1 = 2

sample_part2 = """
abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio
"""

expected_part2 = 3


class TestScript(unittest.TestCase):

    def test_valid_passphrases_part1(self):
        result = valid_passphrases_part1(sample_part1)
        self.assertEqual(result, expected_part1)

    def test_valid_passphrases_part2(self):
        result = valid_passphrases_part2(sample_part2)
        self.assertEqual(result, expected_part2)


if __name__ == '__main__':
    unittest.main()
