"""
Valid Sudoku

Problem Source: LeetCode #36 (https://leetcode.com/problems/valid-sudoku/)
Difficulty: Medium
Category: Hash Table, Array
Date Solved: 2024-07-30

Problem Description:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition
2. Each column must contain the digits 1-9 without repetition
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1 (Valid):
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2 (Invalid):
Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'

Solution Approaches:

Approach 1: Hash Set Tracking (Optimal)
Time Complexity: O(1) - Fixed 9x9 board
Space Complexity: O(1) - Fixed size data structures

Key Insights:
1. Hash Set Efficiency: Using sets to track seen numbers provides O(1) lookup time
2. 3x3 Square Mapping: The key (r // 3, c // 3) efficiently maps cells to their 3x3 square
3. Early Termination: Return False immediately when a violation is found
4. Space Optimization: defaultdict with sets provides clean, readable code

Edge Cases:
- Empty board (all cells are '.')
- Board with only one number
- Duplicate in same row
- Duplicate in same column
- Duplicate in same 3x3 square

Tags: #HashTable #Array #Matrix #Sudoku #Validation #NeetCode150
"""

from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validate if a Sudoku board is valid using hash sets for tracking.

        Args:
            board (List[List[str]]): 9x9 Sudoku board

        Returns:
            bool: True if the board configuration is valid, False otherwise
        """
        # Use defaultdict to track numbers in rows, columns, and 3x3 squares
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # Iterate through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue

                # Check for Sudoku rule violations
                # 1. Number already exists in the same row
                # 2. Number already exists in the same column
                # 3. Number already exists in the same 3x3 square
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # Add number to tracking sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no violations found, board is valid
        return True

    def isValidSudokuAlternative(self, board: List[List[str]]) -> bool:
        """
        Alternative approach using separate validation methods.

        Time Complexity: O(1) - Fixed 9x9 board
        Space Complexity: O(1) - Fixed size data structures

        Args:
            board (List[List[str]]): 9x9 Sudoku board

        Returns:
            bool: True if the board configuration is valid, False otherwise
        """
        # Check rows
        for row in board:
            if not self._is_valid_group(row):
                return False

        # Check columns
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            if not self._is_valid_group(column):
                return False

        # Check 3x3 squares
        for r in (0, 3, 6):
            for c in (0, 3, 6):
                square = [
                    board[r + dr][c + dc]
                    for dr in range(3)
                    for dc in range(3)
                ]
                if not self._is_valid_group(square):
                    return False

        return True

    def _is_valid_group(self, group: List[str]) -> bool:
        """
        Helper method to check if a group (row/column/square) is valid.

        Args:
            group (List[str]): List of 9 cells to check

        Returns:
            bool: True if group is valid, False otherwise
        """
        # Filter out empty cells
        numbers = [num for num in group if num != '.']

        # Check for duplicates
        return len(numbers) == len(set(numbers))


def test_valid_sudoku():
    """
    Comprehensive test cases for Sudoku validator
    """
    solution = Solution()

    # Test cases: (board, expected_result, test_name)
    test_cases = [
        # Valid Sudoku board
        ([
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], True, "Valid Complete Sudoku"),

        # Invalid board - duplicate in row
        ([
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], False, "Duplicate in Row"),

        # Invalid board - duplicate in column
        ([
            ["5","3",".",".","7",".",".",".","."],
            ["5",".",".","1","9","5",".",".","."],  # Duplicate 5 in first column
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], False, "Duplicate in Column"),

        # Invalid board - duplicate in 3x3 square
        ([
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","5",".",".",".",".","6","."],  # Duplicate 5 in top-left square
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ], False, "Duplicate in 3x3 Square"),

        # Empty board
        ([
            ["."] * 9 for _ in range(9)
        ], True, "Empty Board"),

        # Board with single number
        ([
            ["5"] + ["."] * 8,
            *[["."] * 9 for _ in range(8)]
        ], True, "Single Number Board")
    ]

    # Test both solution methods
    methods = [
        solution.isValidSudoku,
        solution.isValidSudokuAlternative
    ]

    # Run tests for each method
    for method in methods:
        print(f"\nTesting method: {method.__name__}")
        for board, expected, test_name in test_cases:
            result = method(board)
            assert result == expected, (
                f"Failed {test_name}: "
                f"Expected {expected}, got {result}"
            )
        print("All tests passed! ✅")


def benchmark_approaches():
    """
    Compare performance of different Sudoku validation approaches
    """
    import time

    solution = Solution()

    # Complete valid board
    valid_board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]

    # Invalid board (duplicate in last row)
    invalid_board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","5"]  # Duplicate 5
    ]

    # Approaches to benchmark
    approaches = [
        ("Hash Set Approach", solution.isValidSudoku),
        ("Alternative Approach", solution.isValidSudokuAlternative)
    ]

    # Run benchmark
    for name, func in approaches:
        # Benchmark valid board
        start = time.time()
        for _ in range(10000):
            func(valid_board)
        end = time.time()
        print(f"{name} (Valid Board): {(end - start) * 1000:.2f}ms")

        # Benchmark invalid board
        start = time.time()
        for _ in range(10000):
            func(invalid_board)
        end = time.time()
        print(f"{name} (Invalid Board): {(end - start) * 1000:.2f}ms")


# Run tests and benchmark when script is executed directly
if __name__ == "__main__":
    print("Valid Sudoku - NeetCode Problem Solution")
    print("=" * 50)

    print("\nRunning Test Cases:")
    test_valid_sudoku()

    print("\nRunning Performance Benchmark:")
    benchmark_approaches()

    print("\nRelated Problems:")
    print("- Sudoku Solver (LeetCode #37) - Hard")
    print("- N-Queens (LeetCode #51) - Hard")
    print("- Valid Parentheses (LeetCode #20) - Easy")