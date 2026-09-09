import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.collections_namedtuple.util import calculate_average_marks

class TestCalculateAverageMarks(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            calculate_average_marks([("John", 85), ("Alice", 90), ("Bob", 78)]),
            84.33
        )

    def test_case_2(self):
        self.assertEqual(
            calculate_average_marks([("David", 92), ("Eva", 88), ("Frank", 95)]),
            91.67
        )

    def test_case_3(self):
        self.assertEqual(
            calculate_average_marks([("Grace", 75), ("Hannah", 80), ("Ian", 70)]),
            75.0
        )
if __name__ == '__main__':
    unittest.main()