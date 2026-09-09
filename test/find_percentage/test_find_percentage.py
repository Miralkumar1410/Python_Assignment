import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.find_percentage.util import average_score

class TestFindPercentage(unittest.TestCase):

    def test_case_1(self):
        student_data = {
            "Krishna": [67, 68, 69],
            "Arjun": [70, 98, 63],
            "Malika": [52, 56, 60]
        }

        self.assertEqual(
            average_score(student_data, "Malika"),
            56.0
        )

    def test_case_2(self):
        student_data = {
            "Harsh": [25, 26.5, 28],
            "Anurag": [26, 28, 30]
        }

        self.assertEqual(
            average_score(student_data, "Harsh"),
            26.5
        )

    def test_case_3(self):
        student_data = {
            "A": [100, 100, 100]
        }

        self.assertEqual(
            average_score(student_data, "A"),
            100.0
        )

    def test_case_4(self):
        student_data = {
            "John": [50, 60, 70]
        }

        self.assertEqual(
            average_score(student_data, "John"),
            60.0
        )

    def test_case_5(self):
        student_data = {
            "Alice": [80, 90, 100]
        }

        self.assertEqual(
            average_score(student_data, "Alice"),
            90.0
        )


if __name__ == "__main__":
    unittest.main()
