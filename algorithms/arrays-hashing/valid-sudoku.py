"""
Problem: Valid Sudoku
Source: LeetCode #
Difficulty: Medium
Date Solved: 2024-07-30


"""

from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validate if a Sudoku board is valid.

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
        Alternative approach to validate Sudoku board.
        Uses separate methods for checking rows, columns, and squares.

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

    # Test cases:
    # (board, expected_result, test_name)
    test_cases = [
        # Valid Sudoku board
        ([
             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ], True, "Valid Complete Sudoku"),

        # Invalid board - duplicate in row
        ([
             ["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ], False, "Duplicate in Row"),

        # Invalid board - duplicate in column
        ([
             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["5", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ], False, "Duplicate in Column"),

        # Invalid board - duplicate in 3x3 square
        ([
             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "5", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ], False, "Duplicate in 3x3 Square"),

        # Empty board
        ([
             [".", ".", ".", ".", ".", ".", ".", ".", "."] * 9
         ], True, "Empty Board"),

        # Board with single number
        ([
             ["5", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."] * 8
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


# Performance benchmark (optional)
def benchmark_approaches():
    """
    Compare performance of different Sudoku validation approaches
    """
    import time

    solution = Solution()

    # Large test board
    valid_board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]

    invalid_board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "5"]  # Last digit changed
    ]

    # Approaches to benchmark
    approaches = [
        ("Original Approach", solution.isValidSudoku),
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
    print("Running Test Cases:")
    test_valid_sudoku()

    print("\nRunning Performance Benchmark:")
    benchmark_approaches()

