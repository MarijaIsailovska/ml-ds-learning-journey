"""
Problem: Contains Duplicate
Source: LeetCode #217
Difficulty: Easy
Date Solved: 2024-07-23

Problem Description:
Given an integer array nums, return true if any value appears at least twice.

Approach:
Hash set to track seen elements - O(1) lookup time.

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            nums.sort()
            i=0
            for i in range (len(nums)-1):
                if(nums[i]==nums[i+1]):
                    return True;
            return False;

# Test cases
if __name__ == "__main__":
    s=Solution()
    assert s.hasDuplicate([1,2,3,1]) == True
    assert s.hasDuplicate([1,2,3,4]) == False
    assert s.hasDuplicate([]) == False
    print("Contains Duplicate: All tests passed! ✅")

"""
Personal Notes:
- Time to solve: ___ minutes
- Key insight: Hash set for O(1) membership testing
- Alternative: Sort then check adjacent elements O(n log n)
"""