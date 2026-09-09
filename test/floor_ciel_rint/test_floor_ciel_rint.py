import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.floor_ciel_rint.util import floor_ceil_rint

class TestFloorCeilRint(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(floor_ceil_rint([1.5, 2.3, 3.7]), ([1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [2.0, 2.0, 4.0]))

    def test_case_2(self):
        self.assertEqual(floor_ceil_rint([-1.5, -2.3, -3.7]), ([-2.0, -3.0, -4.0], [-1.0, -2.0, -3.0], [-2.0, -2.0, -4.0]))

    def test_case_3(self):
        self.assertEqual(floor_ceil_rint([0.1, 0.9, 1.5]), ([0.0, 0.0, 1.0], [1.0, 1.0, 2.0], [0.0, 1.0, 2.0]))
if __name__ == '__main__':
    unittest.main()