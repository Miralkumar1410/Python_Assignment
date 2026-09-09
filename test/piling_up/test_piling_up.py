import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.piling_up.util import piling_up

class TestPilingUp(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            piling_up([[4, 3, 2, 1, 3, 4], [1, 3, 2], [1, 2, 3, 4, 5]]),
            ["Yes", "No", "Yes"]
        )

    def test_case_2(self):
        self.assertEqual(
            piling_up([
                [5, 4, 3, 2, 1],
                [1, 2, 3],
                [3, 2, 1]
            ]),
            ["Yes", "Yes", "Yes"]
    )
    def test_case_3(self):
        self.assertEqual(
            piling_up([[1], [2], [3]]),
            ["Yes", "Yes", "Yes"]
        )
if __name__ == '__main__':
    unittest.main()