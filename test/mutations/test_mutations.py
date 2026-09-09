import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.mutations.util import mutate_string

class TestMutateString(unittest.TestCase):
    def test_case_1(self):
            self.assertEqual(mutate_string("abracadabra", 5, "k"), "abrackdabra")
    
    def test_case_2(self):
            self.assertEqual(mutate_string("hello", 1, "a"), "hallo")
    
    def test_case_3(self):
            self.assertEqual(mutate_string("python", 3, "x"), "pytxon")
    
    def test_case_4(self):
            self.assertEqual(mutate_string("abcdef", 0, "z"), "zbcdef")
    
    def test_case_5(self):
        self.assertEqual(mutate_string("test", 3, "s"), "tess")
        
        
        
        
        

if __name__ == '__main__':
    unittest.main()