import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.string_formatting.util import print_formatted

class TestPrintFormatted(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(print_formatted(5), None)

    def test_case_2(self):
        self.assertEqual(print_formatted(10), None)

    def test_case_3(self):
        self.assertEqual(print_formatted(15), None)

    def test_case_4(self):
        self.assertEqual(print_formatted(20), None)

    def test_case_5(self):
        self.assertEqual(print_formatted(25), None)

if __name__ == '__main__':
    unittest.main()