import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest
from src.lists.util import list_operations

class TestListOperations(unittest.TestCase):
    def test_case_1(self):
        list = []
        commands = [
            ["insert", "0", "5"],
            ["insert", "1", "10"],
            ["insert", "0", "6"],
            ["print"],
            ["remove", "6"],
            ["append", "9"],
            ["append", "1"],
            ["sort"],
            ["print"],
            ["pop"],
            ["reverse"],
            ["print"]
        ]
        expected_outputs = [
            [6, 5, 10],
            [1, 5, 9, 10],
            [9, 5, 1]
        ]
        actual_outputs = []

        for command in commands:
            if command[0] == "print":
                actual_outputs.append(list.copy())
            else:
                list_operations(list, command)

        self.assertEqual(actual_outputs, expected_outputs)
if __name__ == '__main__':  
    unittest.main()