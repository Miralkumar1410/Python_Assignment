import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest
from src.calendar.util import weekday_name

class TestWeekdayName(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(weekday_name(8, 5, 2015), "WEDNESDAY")
        
    def test_case_2(self):
        self.assertEqual(weekday_name(12, 25, 2020), "FRIDAY")
    
    def test_case_3(self):
        self.assertEqual(weekday_name(1, 1, 2000), "SATURDAY")
        
if __name__ == '__main__':
    unittest.main()