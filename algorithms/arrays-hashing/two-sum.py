"""
Problem: Two Sum
Source: LeetCode #1
Difficulty: Easy
Date Solved: 2024-07-23

Problem Description:
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.

Approach:
Use hash map to store value->index mapping. For each number, check if its
complement (target - current number) exists in the hash map.

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - hash map stores at most n elements

Key Insights:
- Hash map provides O(1) average lookup for complement
- Store numbers we've seen with their indices
- Return immediately when complement is found
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in array that sum to target.

        Args:
            nums: List[int] - array of integers
            target: int - target sum

        Returns:
            List[int] - indices of the two numbers that sum to target
        """
        countT = {}  # hash map: value -> index

        for i, n in enumerate(nums):
            diff = target - n  # complement we need to find

            if diff in countT:
                return [countT[diff], i]  # found the pair

            countT[n] = i  # store current number and its index

        return []  # no solution found (shouldn't happen per problem constraints)

# Test cases
def test_two_sum():
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    expected1 = [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
    assert result1 == expected1, f"Test 1 failed: got {result1}, expected {expected1}"

    # Test case 2: Different order
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    expected2 = [1, 2]  # nums[1] + nums[2] = 2 + 4 = 6
    assert result2 == expected2, f"Test 2 failed: got {result2}, expected {expected2}"

    # Test case 3: Same number used twice
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    expected3 = [0, 1]  # nums[0] + nums[1] = 3 + 3 = 6
    assert result3 == expected3, f"Test 3 failed: got {result3}, expected {expected3}"

    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = solution.twoSum(nums4, target4)
    expected4 = [2, 4]  # nums[2] + nums[4] = -3 + (-5) = -8
    assert result4 == expected4, f"Test 4 failed: got {result4}, expected {expected4}"

    print("All test cases passed! ✅")


if __name__ == "__main__":
    test_two_sum()

"""
Personal Reflection:
- Time to solve: ___ minutes
- Difficulty rating (1-5): ___/5
- What I learned: Hash map for complement search pattern
- Mistakes made: 
- Key insight: Single pass is possible by checking complement before storing

Similar Problems to Practice:
- Two Sum II (sorted array - use two pointers instead)
- 3Sum (extend to three numbers)
- Two Sum IV (binary search tree)

Interview Notes:
- Always ask about constraints (array size, number ranges, duplicate values)
- Discuss trade-offs: time vs space complexity
- Mention alternative approaches (brute force, sorting)
- Consider edge cases: empty array, no solution, duplicate numbers
"""