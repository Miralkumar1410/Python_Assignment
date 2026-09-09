import sys
from pathlib import Path
from unittest.mock import patch

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.word_order.util import word_order


class TestWordOrder(unittest.TestCase):

    def test_case_1(self):
        input_data = [
            "bcdef",
            "abcdefg",
            "bcde",
            "bcdef"
        ]

        with patch("builtins.input", side_effect=input_data):
            with patch("builtins.print") as mock_print:
                result = word_order(4)

        self.assertIsNone(result)

        mock_print.assert_any_call(3)
        mock_print.assert_any_call(2, 1, 1)

    def test_case_2(self):
        input_data = [
            "hello",
            "world",
            "hello",
            "python",
            "world"
        ]

        with patch("builtins.input", side_effect=input_data):
            with patch("builtins.print") as mock_print:
                result = word_order(5)

        self.assertIsNone(result)

        mock_print.assert_any_call(3)
        mock_print.assert_any_call(2, 2, 1)


if __name__ == "__main__":
    unittest.main()