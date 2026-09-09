import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.numpy_min_max.util import min_max

class TestMinMax(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            min_max([[1, 2], [3, 4]]),
            (1, 4)
        )
        
    def test_case_2(self):
        self.assertEqual(
            min_max([[5, 6], [7, 8]]),
            (5, 8)
        )

    def test_case_3(self):
        self.assertEqual(
            min_max([[9, 10], [11, 12]]),
            (9, 12)
        )

if __name__ == '__main__':
    unittest.main() 