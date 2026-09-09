import sys
from pathlib import Path
from io import StringIO
from contextlib import redirect_stdout

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest

from src.text_alignment.util import text_alingment


class TestTextAlignment(unittest.TestCase):

    def get_expected_output(self, thickness, c):
        expected = []

        # Top Cone
        for i in range(thickness):
            expected.append(
                (c * i).rjust(thickness - 1)
                + c
                + (c * i).ljust(thickness - 1)
            )

        # Top Pillars
        for i in range(thickness + 1):
            expected.append(
                (c * thickness).center(thickness * 2)
                + (c * thickness).center(thickness * 6)
            )

        # Middle Belt
        for i in range((thickness + 1) // 2):
            expected.append(
                (c * thickness * 5).center(thickness * 6)
            )

        # Bottom Pillars
        for i in range(thickness + 1):
            expected.append(
                (c * thickness).center(thickness * 2)
                + (c * thickness).center(thickness * 6)
            )

        # Bottom Cone
        for i in range(thickness):
            expected.append(
                (
                    (c * (thickness - i - 1)).rjust(thickness)
                    + c
                    + (c * (thickness - i - 1)).ljust(thickness)
                ).rjust(thickness * 6)
            )

        return "\n".join(expected)


    def test_case_1(self):
        output = StringIO()

        with redirect_stdout(output):
            result = text_alingment(5, "H")

        actual_output = output.getvalue().rstrip("\n")

        expected_output = self.get_expected_output(5, "H")

        self.assertIsNone(result)
        self.assertEqual(actual_output, expected_output)


    def test_case_2(self):
        output = StringIO()

        with redirect_stdout(output):
            result = text_alingment(7, "A")

        actual_output = output.getvalue().rstrip("\n")

        expected_output = self.get_expected_output(7, "A")

        self.assertIsNone(result)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()