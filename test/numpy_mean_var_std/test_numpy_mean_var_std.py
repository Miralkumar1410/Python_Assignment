import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest
from unittest.mock import patch

from src.numpy_mean_var_std.util import tools


class TestNumpyMeanVarStd(unittest.TestCase):

    @patch(
        "src.numpy_mean_var_std.util.input",
        side_effect=["1 2", "3 4"]
    )
    def test_case_1(self, mock_input):

        n = 2
        m = 2

        expected_output = (
            [1.5, 3.5],
            [1.0, 1.0],
            1.11803398875
        )

        actual_output = tools(n)

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()