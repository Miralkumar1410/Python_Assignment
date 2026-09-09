import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.linear_algebra.util import lin_alg


class TestLinearAlgebra(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(
            lin_alg([[1, 2], [3, 4]]),
            (-2.0, [[-2.0, 1.0], [1.5, -0.5]])
        )

    def test_case_2(self):
        self.assertEqual(
            lin_alg([[5, 6], [7, 8]]),
            (-2.0, [[-4.0, 3.0], [3.5, -2.5]])
        )

    def test_case_3(self):
        self.assertEqual(
            lin_alg([[9, 10], [11, 12]]),
            (-2.0, [[-6.0, 5.0], [5.5, -4.5]])
        )


if __name__ == '__main__':
    unittest.main()