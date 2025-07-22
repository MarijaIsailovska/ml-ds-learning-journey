"""
Problem: Top K Frequent Elements
Source: LeetCode #347
Difficulty: Medium
Date Solved: 2024-07-23

Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Approach:
Bucket Sort approach using frequency as index:
1. Count frequency of each number using hash map
2. Create buckets where index = frequency, value = list of numbers with that frequency
3. Traverse buckets from highest frequency to lowest, collecting k elements

Time Complexity: O(n) - single pass for counting + single pass for bucketing + at most n elements to collect
Space Complexity: O(n) - hash map + bucket array both use O(n) space

Key Insights:
- Bucket sort is perfect when we know the range (0 to n frequencies)
- Maximum frequency is at most n (all elements are the same)
- Avoids O(n log n) sorting by using frequency as direct index
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find k most frequent elements using bucket sort approach.

        Args:
            nums: List[int] - array of integers
            k: int - number of most frequent elements to return

        Returns:
            List[int] - k most frequent elements in any order
        """
        # Step 1: Count frequency of each number
        Map = {}
        for n in nums:
            Map[n] = 1 + Map.get(n, 0)  # increment count, default to 0

        # Step 2: Create buckets where index = frequency
        # arr[i] contains all numbers that appear exactly i times
        arr = [[] for i in range(len(nums) + 1)]  # max frequency is len(nums)

        # Step 3: Place numbers into buckets based on their frequency
        for n, c in Map.items():  # n = number, c = count/frequency
            arr[c].append(n)

        # Step 4: Collect k most frequent elements from highest frequency buckets
        res = []
        for i in range(len(arr) - 1, 0, -1):  # traverse from highest to lowest frequency
            for n in arr[i]:  # get all numbers with frequency i
                res.append(n)
                if len(res) == k:  # stop when we have k elements
                    return res

        return res  # shouldn't reach here if k is valid


# Alternative approaches for comparison
class AlternativeSolutions:
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Using min-heap approach - O(n log k) time, O(n) space
        """
        import heapq
        from collections import Counter

        # Count frequencies
        count = Counter(nums)

        # Use min-heap to keep top k frequent elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]

    def topKFrequentSorting(self, nums: List[int], k: int) -> List[int]:
        """
        Simple sorting approach - O(n log n) time, O(n) space
        """
        from collections import Counter

        count = Counter(nums)
        # Sort by frequency (descending) and take first k
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in sorted_items[:k]]

    def topKFrequentQuickSelect(self, nums: List[int], k: int) -> List[int]:
        """
        Quick Select approach - O(n) average, O(n²) worst case
        """
        from collections import Counter
        import random

        count = Counter(nums)
        unique_nums = list(count.keys())

        def quickselect(left, right, k_smallest):
            # Base case: only one element
            if left == right:
                return

            # Choose random pivot
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            # Pivot is in its final sorted position
            if k_smallest == pivot_idx:
                return
            elif k_smallest < pivot_idx:
                quickselect(left, pivot_idx - 1, k_smallest)
            else:
                quickselect(pivot_idx + 1, right, k_smallest)

        def partition(left, right, pivot_idx):
            pivot_freq = count[unique_nums[pivot_idx]]
            # Move pivot to end
            unique_nums[pivot_idx], unique_nums[right] = unique_nums[right], unique_nums[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if count[unique_nums[i]] < pivot_freq:
                    unique_nums[store_idx], unique_nums[i] = unique_nums[i], unique_nums[store_idx]
                    store_idx += 1

            # Move pivot to its final place
            unique_nums[right], unique_nums[store_idx] = unique_nums[store_idx], unique_nums[right]
            return store_idx

        n = len(unique_nums)
        quickselect(0, n - 1, n - k)
        return unique_nums[n - k:]


# Test cases
def test_top_k_frequent():
    solution = Solution()

    def sort_result(result):
        """Helper to sort result for comparison since order doesn't matter"""
        return sorted(result)

    # Test case 1: Basic example
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    expected1 = [1, 2]  # 1 appears 3 times, 2 appears 2 times
    assert sort_result(result1) == sort_result(expected1), f"Test 1 failed: got {result1}, expected {expected1}"

    # Test case 2: Single element
    nums2 = [1]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    expected2 = [1]
    assert result2 == expected2, f"Test 2 failed: got {result2}, expected {expected2}"

    # Test case 3: All elements have same frequency
    nums3 = [1, 2, 3]
    k3 = 2
    result3 = solution.topKFrequent(nums3, k3)
    # Any 2 elements are valid since all have frequency 1
    assert len(result3) == 2, f"Test 3 failed: should return 2 elements"
    assert all(x in [1, 2, 3] for x in result3), f"Test 3 failed: invalid elements"

    # Test case 4: k equals number of unique elements
    nums4 = [4, 1, -1, 2, -1, 2, 3]
    k4 = 4
    result4 = solution.topKFrequent(nums4, k4)
    # Should return all unique elements: -1, 2, 1, 3, 4
    assert len(result4) == 4, f"Test 4 failed: should return 4 elements"

    # Test case 5: Negative numbers
    nums5 = [-1, -1, -2, -2, -2, 0]
    k5 = 2
    result5 = solution.topKFrequent(nums5, k5)
    expected5 = [-2, -1]  # -2 appears 3 times, -1 appears 2 times
    assert sort_result(result5) == sort_result(expected5), f"Test 5 failed: got {result5}, expected {expected5}"

    print("All test cases passed! ✅")


# Performance and approach analysis
def analyze_approaches():
    """
    Compare different approaches for Top K Frequent Elements
    """
    print("Approach Comparison:")
    print("\n1. Bucket Sort (Your approach):")
    print("   - Time: O(n)")
    print("   - Space: O(n)")
    print("   - Pros: Optimal time complexity, simple logic")
    print("   - Cons: Uses extra space for buckets")

    print("\n2. Min-Heap:")
    print("   - Time: O(n log k)")
    print("   - Space: O(k)")
    print("   - Pros: Space efficient when k << n")
    print("   - Cons: Slower than bucket sort")

    print("\n3. Sorting:")
    print("   - Time: O(n log n)")
    print("   - Space: O(n)")
    print("   - Pros: Simple to implement")
    print("   - Cons: Not optimal time complexity")

    print("\n4. Quick Select:")
    print("   - Time: O(n) average, O(n²) worst")
    print("   - Space: O(n)")
    print("   - Pros: Can be optimal on average")
    print("   - Cons: Complex implementation, worst case is bad")

    print("\nYour bucket sort approach is excellent because:")
    print("- Achieves optimal O(n) time complexity")
    print("- Intuitive and easy to understand")
    print("- Handles all edge cases naturally")
    print("- Smart use of frequency as array index")


if __name__ == "__main__":
    test_top_k_frequent()
    print("\n" + "=" * 60)
    analyze_approaches()

"""
Personal Reflection:
- Time to solve: ___ minutes
- Difficulty rating (1-5): ___/5
- What I learned: Bucket sort technique using frequency as index
- Mistakes made: 
- Key insight: When range is known (0 to n), bucket sort achieves O(n) time

Your Code Brilliance:
1. **Optimal Algorithm Choice:** Bucket sort for O(n) time complexity
   - Recognizes that max frequency is n (length of array)
   - Uses frequency directly as array index - genius!

2. **Smart Data Structures:**
   - Hash map for O(1) frequency counting
   - Array of lists for O(1) bucket access
   - No need for sorting or heap operations

3. **Efficient Implementation:**
   - Single pass for counting: O(n)
   - Single pass for bucketing: O(n)
   - At most n elements to collect: O(n)
   - Total: O(n) - optimal!

4. **Clean Traversal Logic:**
   - Traverse from highest to lowest frequency
   - Early termination when k elements found
   - Handles ties naturally (order doesn't matter)

Code Quality: 10/10
- Demonstrates deep algorithmic thinking
- Shows understanding of time/space trade-offs
- Clean, readable implementation
- Optimal solution to a medium problem

Why This Approach Rocks:
- Faster than heap-based solutions O(n log k)
- Faster than sorting-based solutions O(n log n)
- Simpler than quickselect implementation
- Natural handling of equal frequencies

Similar Problems to Practice:
- Kth Largest Element in Array (quickselect/heap)
- Sort Characters by Frequency (similar bucketing)
- Find K Closest Points to Origin (heap/quickselect)

Interview Notes:
- Explain the key insight: frequency range is 0 to n
- Discuss why bucket sort is perfect here
- Compare with other approaches and their trade-offs
- Show understanding of when each approach is best
- Mention that this demonstrates "thinking outside the box"
"""