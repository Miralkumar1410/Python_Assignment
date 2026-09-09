import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.merge_the_tools.util import merge_the_tools

class TestMergeTheTools(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            merge_the_tools("AABCAAADA", 3),
            ["AB", "CA", "AD"]
        )

    def test_case_2(self):
        self.assertEqual(
            merge_the_tools("ABABABAB", 2),
            ["AB", "AB", "AB", "AB"]
        )

    def test_case_3(self):
        self.assertEqual(
            merge_the_tools("AAABBBCCC", 3),
            ["A", "B", "C"]
        )

    def test_case_4(self):
        self.assertEqual(
            merge_the_tools("ABCDEABCDE", 5),
            ["ABCDE", "ABCDE"]
        )

    def test_case_5(self):
        self.assertEqual(
            merge_the_tools("AABBCCDD", 2),
            ["A", "B", "C", "D"]
        )

if __name__ == '__main__':
    unittest.main()