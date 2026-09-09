import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.text_alignment.util import text_alingment

class TestTextAlignment(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(text_alingment(5, 'H'), None)

    def test_case_2(self):
        self.assertEqual(text_alingment(7, 'A'), None)

    def test_case_3(self):
        self.assertEqual(text_alingment(9, 'B'), None)

    def test_case_4(self):
        self.assertEqual(text_alingment(11, 'C'), None)

    def test_case_5(self):
        self.assertEqual(text_alingment(13, 'D'), None)

if __name__ == '__main__':
    unittest.main()