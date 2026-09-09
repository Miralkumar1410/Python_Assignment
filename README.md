# Python Assignment

A structured Python practice repository containing **19 programming
problems** with separate implementation and test files. The problems are
based on the assignment documented in the accompanying Python Assignment
documentation.

The repository follows a simple separation of concerns:

-   `src/` contains the implementation for each problem.
-   `tests/` contains `unittest` test cases for each problem.
-   Each problem has a `driver.py` for input/output handling and a
    `util.py` for the core solution logic.

## Repository Structure

``` text
Python_Assignment/
│
├── src/
│   ├── calendar/
│   │   ├── driver.py
│   │   └── util.py
│   ├── collections_namedtuple/
│   │   ├── driver.py
│   │   └── util.py
│   ├── find_percentage/
│   │   ├── driver.py
│   │   └── util.py
│   ├── floor_ciel_rint/
│   │   ├── driver.py
│   │   └── util.py
│   ├── iterables_and_iterators/
│   │   ├── driver.py
│   │   └── util.py
│   ├── linear_algebra/
│   │   ├── driver.py
│   │   └── util.py
│   ├── lists/
│   │   ├── driver.py
│   │   └── util.py
│   ├── merge_the_tools/
│   │   ├── driver.py
│   │   └── util.py
│   ├── mutations/
│   │   ├── driver.py
│   │   └── util.py
│   ├── no_idea/
│   │   ├── driver.py
│   │   └── util.py
│   ├── numpy_mean_var_std/
│   │   ├── driver.py
│   │   └── util.py
│   ├── numpy_min_max/
│   │   ├── driver.py
│   │   └── util.py
│   ├── piling_up/
│   │   ├── driver.py
│   │   └── util.py
│   ├── runner_up/
│   │   ├── driver.py
│   │   └── util.py
│   ├── string_formatting/
│   │   ├── driver.py
│   │   └── util.py
│   ├── text_alignment/
│   │   ├── driver.py
│   │   └── util.py
│   ├── time_delta/
│   │   ├── driver.py
│   │   └── util.py
│   ├── validate_email/
│   │   ├── driver.py
│   │   └── util.py
│   └── word_order/
│       ├── driver.py
│       └── util.py
│
└── tests/
    ├── calendar/
    │   └── test_calendar.py
    ├── collections_namedtuple/
    │   └── test_collections_namedtuple.py
    ├── find_percentage/
    │   └── test_find_percentage.py
    ├── floor_ciel_rint/
    │   └── test_floor_ciel_rint.py
    ├── iterables_and_iterators/
    │   └── test_iterables_and_iterators.py
    ├── linear_algebra/
    │   └── test_linear_algebra.py
    ├── lists/
    │   └── test_lists.py
    ├── merge_the_tools/
    │   └── test_merge_the_tools.py
    ├── mutations/
    │   └── test_mutations.py
    ├── no_idea/
    │   └── test_no_idea.py
    ├── numpy_mean_var_std/
    │   └── test_numpy_mean_var_std.py
    ├── numpy_min_max/
    │   └── test_numpy_min_max.py
    ├── piling_up/
    │   └── test_piling_up.py
    ├── runner_up/
    │   └── test_runner_up.py
    ├── string_formatting/
    │   └── test_string_formatting.py
    ├── text_alignment/
    │   └── test_text_alignment.py
    ├── time_delta/
    │   └── test_time_delta.py
    ├── validate_email/
    │   └── test_validate_email.py
    └── word_order/
        └── test_word_order.py
```

## Problems Covered

  ------------------------------------------------------------------------------
  \#                      Problem                    Main Concepts
  ----------------------- -------------------------- ---------------------------
  1                       Lists                      List operations: insert,
                                                     print, remove, append,
                                                     sort, pop, reverse

  2                       Finding the Percentage     Dictionaries, lists,
                                                     average calculation,
                                                     rounding

  3                       Find the Runner-Up Score!  Iteration, maximum and
                                                     runner-up tracking

  4                       Mutations                  Strings, list conversion,
                                                     character replacement

  5                       Merge the Tools            String slicing, grouping,
                                                     duplicate removal

  6                       String Formatting          Decimal, octal,
                                                     hexadecimal, binary
                                                     conversion and formatting

  7                       Text Alignment             String alignment,
                                                     `rjust()`, `ljust()`,
                                                     `center()`

  8                       Calendar Module            Python `calendar` module
                                                     and weekday calculation

  9                       Collections.namedtuple()   `namedtuple`, records,
                                                     average calculation

  10                      Time Delta                 `datetime`, timestamp
                                                     parsing, timezone offsets,
                                                     seconds

  11                      Floor, Ceil and Rint       NumPy `floor()`, `ceil()`,
                                                     and `rint()`

  12                      Min and Max                NumPy arrays, minimum
                                                     values, maximum aggregation

  13                      Linear Algebra             NumPy linear algebra,
                                                     determinant and matrix
                                                     inverse

  14                      Mean, Var, and Std         NumPy mean, variance,
                                                     standard deviation, axes

  15                      No Idea!                   Sets and membership
                                                     operations

  16                      Word Order                 Word counting, distinct
                                                     words, occurrence frequency

  17                      Piling Up                  `deque`, stack-like
                                                     selection, comparison of
                                                     cube sizes

  18                      Iterables and Iterators    `itertools.combinations`,
                                                     probability calculation

  19                      Validating Email Addresses Validation logic,
                          With a Filter              `filter()`, sorting
  ------------------------------------------------------------------------------

## Implementation Approach

Each problem is divided into two files:

### `util.py`

Contains the reusable function that implements the core problem logic.

For example:

``` python
def average_score(student_marks, query_name):
    marks = student_marks[query_name]
    return round(sum(marks) / len(marks), 2)
```

### `driver.py`

Handles input, prepares the required data structure, calls the utility
function, and prints or writes the result.

This separation keeps the solution logic independent from input/output
handling and makes the functions easier to test.

## Testing

The assignment uses Python's built-in `unittest` framework.

Each problem has its own test module under `tests/`. The documented test
cases use assertions such as `assertEqual()` and include multiple inputs
for several problems.

A typical test follows this pattern:

``` python
import unittest

class TestExample(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(function_name(input_data), expected_output)


if __name__ == "__main__":
    unittest.main()
```

### Run an individual test

From the repository root:

``` bash
python -m unittest tests/lists/test_lists.py
```

Replace the path with the required test file.

### Run all tests

``` bash
python -m unittest discover -s tests
```

If the project imports require the repository root to be on
`PYTHONPATH`, run:

``` bash
python -m unittest discover -s tests -p "test_*.py"
```

## Key Python Concepts Practiced

This assignment provides hands-on practice with:

-   Lists and list methods
-   Dictionaries
-   Sets
-   Strings and string formatting
-   Functions
-   Loops and conditional statements
-   `datetime`
-   `calendar`
-   `collections.namedtuple`
-   `collections.deque`
-   `itertools.combinations`
-   Lambda/filter concepts
-   NumPy arrays and mathematical operations
-   Unit testing with `unittest`
-   Separation of input/output code from reusable logic

## Problem-wise Summary

### 1. Lists

The solution processes commands and performs common list operations
including `insert`, `print`, `remove`, `append`, `sort`, `pop`, and
`reverse`.

### 2. Finding the Percentage

Student names and their marks are stored in a dictionary. The required
student's average is calculated and rounded to two decimal places.

### 3. Find the Runner-Up Score!

The implementation tracks the highest and second-highest distinct values
while iterating through the scores.

### 4. Mutations

The input string is converted into a list so that the character at the
specified position can be replaced, after which the characters are
joined back into a string.

### 5. Merge the Tools

The input string is processed in fixed-size groups. A set is used to
ensure that repeated characters within a group are included only once
while maintaining their encountered order.

### 6. String Formatting

Numbers from `1` through `n` are displayed in decimal, octal,
hexadecimal, and binary formats. A calculated field width is used to
align the output.

### 7. Text Alignment

The HackerRank-style logo is generated using right, left, and center
string alignment operations.

### 8. Calendar Module

Python's `calendar` module is used to determine the weekday for a given
month, day, and year, with the result converted to uppercase.

### 9. Collections.namedtuple()

Student information is represented as records, and the marks are
aggregated to calculate the average.

### 10. Time Delta

Timezone-aware date-time strings are parsed using `datetime.strptime()`.
The absolute difference between the two timestamps is converted into
seconds.

### 11. Floor, Ceil and Rint

NumPy is used to calculate the floor, ceiling, and nearest-integer
values of the input array.

### 12. Min and Max

The input is represented as a NumPy array. The minimum values are
determined and the maximum among those values is returned.

### 13. Linear Algebra

The solution uses NumPy's linear algebra functionality to work with a
matrix and calculate its determinant and inverse, with values rounded to
two decimal places.

### 14. Mean, Var, and Std

NumPy functions calculate the mean along one axis, variance along
another axis, and standard deviation of the complete array.

### 15. No Idea!

The solution uses sets for membership checking. Happiness is increased
for elements in set `A` and decreased for elements in set `B`.

### 16. Word Order

Words are processed in input order. The solution tracks distinct words
and the number of occurrences of each word.

### 17. Piling Up

A deque is used to select blocks from either end. The selected blocks
are checked to determine whether they can be arranged in non-increasing
order.

### 18. Iterables and Iterators

Combinations are generated from the input letters. The probability that
at least one selected position contains the letter `a` is calculated.

### 19. Validating Email Addresses With a Filter

Email strings are checked against the required username, website, and
extension rules. Valid addresses are filtered and sorted.

## Dependencies

The solutions documented in the assignment use standard Python
functionality along with NumPy for the numerical problems.

Install NumPy with:

``` bash
pip install numpy
```

The following Python modules are used directly by the solutions:

-   `calendar`
-   `datetime`
-   `collections`
-   `itertools`
-   `unittest`
-   `numpy`

Most of these are part of Python's standard library; NumPy is an
external dependency.

## Purpose

The repository is intended to provide structured practice in Python
programming by combining:

1.  Problem solving
2.  Modular Python development
3.  Input/output handling
4.  Reusable utility functions
5.  Unit testing
6.  NumPy-based numerical programming

The accompanying documentation records the problem statements,
implementations, test cases, and test outputs for the 19 exercises.
