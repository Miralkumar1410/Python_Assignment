import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.runner_up.util import runner_up_score

class TestRunnerUpScore(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(runner_up_score([2, 3, 6, 6, 5]), 5)

    def test_case_2(self):
        self.assertEqual(runner_up_score([1, 2, 3, 4, 5]), 4)

    def test_case_3(self):
        self.assertEqual(runner_up_score([10, 10, 10]), float('-inf'))

    def test_case_4(self):
        self.assertEqual(runner_up_score([-1, -2, -3]), -2)

    def test_case_5(self):
        self.assertEqual(runner_up_score([100]), float('-inf'))
        
if __name__ == '__main__':
    unittest.main()