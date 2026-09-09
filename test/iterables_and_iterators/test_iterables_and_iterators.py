import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.iterables_and_iterators.util import itertools


class TestItertools(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(
            itertools("ABCD", 3),
            "0.750"
        )

    def test_case_2(self):
        self.assertEqual(
            itertools("XYZ", 2),
            "0.000"
        )

    def test_case_3(self):
        self.assertEqual(
            itertools("PQRS", 4),
            "0.000"
        )

    def test_case_4(self):
        self.assertEqual(
            itertools("LMN", 1),
            "0.000"
        )

    def test_case_5(self):
        self.assertEqual(
            itertools("ABCDE", 5),
            "1.000"
        )


if __name__ == '__main__':
    unittest.main()