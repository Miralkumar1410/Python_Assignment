import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest
from src.time_delta.util import time_delta

class TestTimeDelta(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"), "25200")

    def test_case_2(self):
        self.assertEqual(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"), "88200")

    def test_case_3(self):
        self.assertEqual(time_delta("Fri 01 May 2015 13:54:36 -0000", "Sat 02 May 2015 19:54:36 +0530"), "88200")

    def test_case_4(self):
        self.assertEqual(time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"), "25200")

    def test_case_5(self):
        self.assertEqual(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"), "88200")
if __name__ == '__main__':  
    unittest.main()
