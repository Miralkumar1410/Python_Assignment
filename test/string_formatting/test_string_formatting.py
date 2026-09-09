import sys
from pathlib import Path
from unittest.mock import patch

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.string_formatting.util import print_formatted


class TestPrintFormatted(unittest.TestCase):

    def test_case_1(self):
        expected_output = (
    "  1   1   1   1\n"
    "  2   2   2  10\n"
    "  3   3   3  11\n"
    "  4   4   4 100\n"
    "  5   5   5 101"
)

        with patch("builtins.print") as mock_print:
            print_formatted(5)

        actual_output = "\n".join(
            call.args[0] for call in mock_print.call_args_list
        )

        self.assertEqual(actual_output, expected_output)

    def test_case_2(self):
        expected_output = (
            "   1    1    1    1\n"
            "   2    2    2   10\n"
            "   3    3    3   11\n"
            "   4    4    4  100\n"
            "   5    5    5  101\n"
            "   6    6    6  110\n"
            "   7    7    7  111\n"
            "   8   10    8 1000\n"
            "   9   11    9 1001\n"
            "  10   12    A 1010"
        )

        with patch("builtins.print") as mock_print:
            print_formatted(10)

        actual_output = "\n".join(
            call.args[0] for call in mock_print.call_args_list
        )

        self.assertEqual(actual_output, expected_output)

    def test_case_3(self):
        expected_output = (
    "   1    1    1    1\n"
    "   2    2    2   10\n"
    "   3    3    3   11\n"
    "   4    4    4  100\n"
    "   5    5    5  101\n"
    "   6    6    6  110\n"
    "   7    7    7  111\n"
    "   8   10    8 1000\n"
    "   9   11    9 1001\n"
    "  10   12    A 1010\n"
    "  11   13    B 1011\n"
    "  12   14    C 1100\n"
    "  13   15    D 1101\n"
    "  14   16    E 1110\n"
    "  15   17    F 1111"
)

        with patch("builtins.print") as mock_print:
            print_formatted(15)

        actual_output = "\n".join(
            call.args[0] for call in mock_print.call_args_list
        )

        self.assertEqual(actual_output, expected_output)

    
if __name__ == '__main__':
    unittest.main()