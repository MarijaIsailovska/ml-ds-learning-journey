"""
Longest Consecutive Sequence

Problem Source: LeetCode #128 (https://leetcode.com/problems/longest-consecutive-sequence/)
Difficulty: Medium
Category: Array, Hash Table, Union Find
Date Solved: 2024-08-04

Problem Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time complexity.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 6
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4, 100, 200]. Therefore its length is 6.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Key Insights:
1. Hash Set for O(1) Lookup: Convert array to set for constant time membership checks
2. Smart Starting Point: Only start counting from numbers that are the beginning of a sequence (num-1 not in set)
3. Greedy Extension: Once we find a sequence start, extend it as far as possible
4. Avoid Duplicates: Using set automatically handles duplicate numbers
5. Time Optimization: Each number is visited at most twice (once as potential start, once during extension)

Algorithm Approach:
1. Convert nums to set for O(1) lookups
2. For each number, check if it's the start of a sequence (num-1 not in set)
3. If it's a start, count consecutive numbers by incrementing until no longer in set
4. Track the maximum sequence length found

Time Complexity: O(n) - Each number visited at most twice
Space Complexity: O(n) - For the hash set

Edge Cases:
- Empty array: return 0
- Single element: return 1
- All elements same: return 1
- No consecutive elements: return 1
- Array with duplicates: handled by set conversion

Tags: #Array #HashTable #Sequence #Consecutive #NeetCode150 #Blind75
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the length of the longest consecutive elements sequence.

        Uses hash set approach to achieve O(n) time complexity by:
        1. Converting array to set for O(1) lookups
        2. Only starting sequences from their beginning numbers
        3. Extending sequences greedily once started

        Args:
            nums (List[int]): Array of integers (can contain duplicates)

        Returns:
            int: Length of longest consecutive sequence

        Example:
            >>> solution = Solution()
            >>> solution.longestConsecutive([100,4,200,1,3,2])
            6
            >>> solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
            9
        """
        # Handle empty array edge case
        if not nums:
            return 0

        # Convert to set for O(1) membership checks and duplicate removal
        num_set = set(nums)
        longest = 0

        # Check each unique number as potential sequence start
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            # (i.e., num-1 is not in the set)
            if num - 1 not in num_set:  # почеток на секвенца (start of sequence)
                current_num = num
                current_streak = 1

                # Extend the sequence as far as possible
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update longest sequence found so far
                longest = max(longest, current_streak)

        return longest

    def longestConsecutiveAlternative(self, nums: List[int]) -> int:
        """
        Alternative approach using sorting (for comparison).

        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) if sorting in-place allowed, O(n) otherwise

        Args:
            nums (List[int]): Array of integers

        Returns:
            int: Length of longest consecutive sequence
        """
        if not nums:
            return 0

        # Sort the array
        nums.sort()

        longest = 1
        current_streak = 1

        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i-1]:
                continue
            # Check if consecutive
            elif nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                # Reset streak
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest, current_streak)

    def longestConsecutiveUnionFind(self, nums: List[int]) -> int:
        """
        Union-Find approach (for educational purposes).

        Time Complexity: O(n * α(n)) where α is inverse Ackermann function
        Space Complexity: O(n)

        Args:
            nums (List[int]): Array of integers

        Returns:
            int: Length of longest consecutive sequence
        """
        if not nums:
            return 0

        # Remove duplicates
        unique_nums = list(set(nums))
        n = len(unique_nums)

        # Create number to index mapping
        num_to_idx = {num: i for i, num in enumerate(unique_nums)}

        # Union-Find data structure
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]

        # Union consecutive numbers
        for num in unique_nums:
            if num + 1 in num_to_idx:
                union(num_to_idx[num], num_to_idx[num + 1])

        # Find maximum component size
        return max(size[find(i)] for i in range(n))


def test_longest_consecutive():
    """
    Comprehensive test cases for longest consecutive sequence
    """
    solution = Solution()

    # Test cases: (input, expected_output, test_name)
    test_cases = [
        # Basic examples
        ([100, 4, 200, 1, 3, 2], 6, "Example 1 - Mixed numbers"),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, "Example 2 - With duplicates"),

        # Edge cases
        ([], 0, "Empty array"),
        ([1], 1, "Single element"),
        ([1, 1, 1, 1], 1, "All duplicates"),
        ([1, 3, 5, 7, 9], 1, "No consecutive elements"),

        # Sequential cases
        ([1, 2, 3, 4, 5], 5, "Perfect sequence"),
        ([5, 4, 3, 2, 1], 5, "Reverse sequence"),
        ([1, 2, 4, 5, 6], 3, "Two sequences"),

        # Negative numbers
        ([-1, -2, -3, 0, 1], 5, "Negative and positive"),
        ([-5, -4, -3, -1], 3, "Only negatives"),

        # Large gaps
        ([1, 1000000, 2, 3, 4], 4, "Large gaps"),
        ([2147483647, -2147483648, 0], 1, "Extreme values"),

        # Complex cases
        ([9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7], 4, "Complex mixed"),
        ([1, 9, 3, 10, 4, 20, 2], 4, "Multiple sequences")
    ]

    # Test all approaches
    methods = [
        ("Hash Set Approach", solution.longestConsecutive),
        ("Sorting Approach", solution.longestConsecutiveAlternative),
        ("Union-Find Approach", solution.longestConsecutiveUnionFind)
    ]

    for method_name, method in methods:
        print(f"\nTesting {method_name}:")
        for nums, expected, test_name in test_cases:
            result = method(nums.copy())  # Copy to avoid modification
            assert result == expected, (
                f"Failed {test_name}: "
                f"Expected {expected}, got {result} for input {nums}"
            )
        print("All tests passed! ✅")


def benchmark_approaches():
    """
    Performance comparison of different approaches
    """
    import time
    import random

    solution = Solution()

    # Generate test data
    test_sizes = [100, 1000, 10000]

    for size in test_sizes:
        print(f"\nBenchmarking with array size: {size}")

        # Generate random test data
        nums = [random.randint(-size, size) for _ in range(size)]

        # Test approaches
        approaches = [
            ("Hash Set O(n)", solution.longestConsecutive),
            ("Sorting O(n log n)", solution.longestConsecutiveAlternative),
            ("Union-Find O(n α(n))", solution.longestConsecutiveUnionFind)
        ]

        for name, func in approaches:
            start = time.time()
            result = func(nums.copy())
            end = time.time()
            print(f"{name:20}: {(end - start) * 1000:7.2f}ms (result: {result})")


def analyze_algorithm():
    """
    Step-by-step analysis of the hash set approach
    """
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]

    print("Algorithm Analysis:")
    print(f"Input: {nums}")
    print(f"Set conversion: {set(nums)}")
    print()

    num_set = set(nums)
    longest = 0

    print("Step-by-step execution:")
    for num in sorted(num_set):  # Sort for clearer output
        if num - 1 not in num_set:
            print(f"Number {num}: Start of sequence (since {num-1} not in set)")
            current_num = num
            current_streak = 1
            sequence = [num]

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                sequence.append(current_num)

            print(f"  Sequence found: {sequence}")
            print(f"  Length: {current_streak}")
            longest = max(longest, current_streak)
        else:
            print(f"Number {num}: Skip (since {num-1} is in set - not sequence start)")

    print(f"\nFinal result: {longest}")


# Run tests and analysis when script is executed directly
if __name__ == "__main__":
    print("Longest Consecutive Sequence - NeetCode Problem Solution")
    print("=" * 60)

    print("\nAlgorithm Step-by-Step Analysis:")
    analyze_algorithm()

    print("\n" + "=" * 60)
    print("Running Test Cases:")
    test_longest_consecutive()

    print("\n" + "=" * 60)
    print("Performance Benchmark:")
    benchmark_approaches()

    print("\n" + "=" * 60)
    print("Related Problems:")
    print("- Binary Tree Longest Consecutive Sequence (LeetCode #298)")
    print("- Longest Consecutive Sequence II (LeetCode #549)")
    print("- Maximum Length of Repeated Subarray (LeetCode #718)")
    print("- Longest Increasing Subsequence (LeetCode #300)")