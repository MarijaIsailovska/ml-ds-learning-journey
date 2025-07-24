"""
Problem: Product of Array Except Self
Source: LeetCode #238
Difficulty: Medium
Date Solved: 2024-07-23

Problem Description:
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operator.

Approach:
Two-pass prefix/postfix approach using single result array:
1. First pass: Calculate prefix products (product of all elements to the left)
2. Second pass: Multiply by postfix products (product of all elements to the right)

Time Complexity: O(n) - two passes through the array
Space Complexity: O(1) - only using the result array (not counting output space)

Key Insights:
- answer[i] = (product of elements to left) × (product of elements to right)
- Use result array to store prefix products, then multiply by postfix
- Avoid division operator by calculating prefix and postfix separately
- Brilliant space optimization: reuse result array for both passes
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product of array except self using prefix/postfix approach.

        Args:
            nums: List[int] - input array of integers

        Returns:
            List[int] - array where result[i] = product of all nums except nums[i]
        """
        # Initialize result array with 1s
        res = [1] * (len(nums))

        # First pass: Calculate prefix products
        # res[i] will contain product of all elements to the left of i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix              # store current prefix product
            prefix *= nums[i]            # update prefix for next iteration

        # Second pass: Multiply by postfix products
        # res[i] *= product of all elements to the right of i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # traverse right to left
            res[i] *= postfix           # multiply existing prefix by postfix
            postfix *= nums[i]          # update postfix for next iteration

        return res


# Alternative approaches for comparison
class AlternativeSolutions:
    def productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
        """
        Brute force approach - O(n²) time, not recommended
        """
        result = []
        n = len(nums)

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:  # skip current element
                    product *= nums[j]
            result.append(product)

        return result

    def productExceptSelfDivision(self, nums: List[int]) -> List[int]:
        """
        Division approach - O(n) time but uses division (not allowed in problem)
        """
        # Calculate total product
        total_product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        result = []
        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                result.append(total_product if num == 0 else 0)
            else:
                result.append(total_product // num)

        return result

    def productExceptSelfTwoArrays(self, nums: List[int]) -> List[int]:
        """
        Two separate arrays approach - O(n) time, O(n) extra space
        """
        n = len(nums)

        # Calculate prefix products
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # Calculate postfix products
        postfix = [1] * n
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        # Combine prefix and postfix
        result = []
        for i in range(n):
            result.append(prefix[i] * postfix[i])

        return result


# Visualization helper
def visualize_solution(nums):
    """
    Step-by-step visualization of the algorithm
    """
    print(f"Input: {nums}")
    n = len(nums)

    # Step 1: Prefix calculation
    res = [1] * n
    prefix = 1
    print(f"\nStep 1 - Prefix calculation:")
    print(f"Initial res: {res}")

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
        print(f"  i={i}: res[{i}] = {res[i]}, prefix becomes {prefix}")

    print(f"After prefix pass: {res}")

    # Step 2: Postfix calculation
    postfix = 1
    print(f"\nStep 2 - Postfix calculation:")

    for i in range(n - 1, -1, -1):
        print(f"  i={i}: res[{i}] = {res[i]} * {postfix} = {res[i] * postfix}")
        res[i] *= postfix
        postfix *= nums[i]
        print(f"        postfix becomes {postfix}")

    print(f"Final result: {res}")
    return res


# Test cases
def test_product_except_self():
    solution = Solution()

    # Test case 1: Basic example
    nums1 = [1, 2, 3, 4]
    result1 = solution.productExceptSelf(nums1)
    expected1 = [24, 12, 8, 6]  # [2*3*4, 1*3*4, 1*2*4, 1*2*3]
    assert result1 == expected1, f"Test 1 failed: got {result1}, expected {expected1}"
    print(f"Test 1 ✅: {nums1} -> {result1}")

    # Test case 2: Contains zero
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.productExceptSelf(nums2)
    expected2 = [0, 0, 9, 0, 0]  # only index 2 gets non-zero (product without the 0)
    assert result2 == expected2, f"Test 2 failed: got {result2}, expected {expected2}"
    print(f"Test 2 ✅: {nums2} -> {result2}")

    # Test case 3: Two elements
    nums3 = [1, 2]
    result3 = solution.productExceptSelf(nums3)
    expected3 = [2, 1]
    assert result3 == expected3, f"Test 3 failed: got {result3}, expected {expected3}"
    print(f"Test 3 ✅: {nums3} -> {result3}")

    # Test case 4: All negative
    nums4 = [-1, -2, -3]
    result4 = solution.productExceptSelf(nums4)
    expected4 = [6, 3, 2]  # [(-2)*(-3), (-1)*(-3), (-1)*(-2)]
    assert result4 == expected4, f"Test 4 failed: got {result4}, expected {expected4}"
    print(f"Test 4 ✅: {nums4} -> {result4}")

    # Test case 5: Multiple zeros
    nums5 = [0, 0, 2, 3]
    result5 = solution.productExceptSelf(nums5)
    expected5 = [0, 0, 0, 0]  # more than one zero makes all products zero
    assert result5 == expected5, f"Test 5 failed: got {result5}, expected {expected5}"
    print(f"Test 5 ✅: {nums5} -> {result5}")

    print("All test cases passed! ✅")


# Performance analysis
def analyze_complexity():
    """
    Analyze why this approach is optimal
    """
    print("\nComplexity Analysis:")
    print("Time Complexity: O(n)")
    print("  - First pass through array: O(n)")
    print("  - Second pass through array: O(n)")
    print("  - Total: O(n) + O(n) = O(n)")

    print("\nSpace Complexity: O(1) extra space")
    print("  - Only using variables: prefix, postfix")
    print("  - Result array doesn't count as extra space")
    print("  - No additional data structures needed")

    print("\nWhy this approach is brilliant:")
    print("1. Avoids division operator (as required)")
    print("2. Handles zeros naturally")
    print("3. Optimal time and space complexity")
    print("4. Uses result array efficiently for two purposes")
    print("5. Easy to understand and implement")


def run_visualization():
    """
    Run the step-by-step visualization
    """
    print("\n" + "="*60)
    print("ALGORITHM VISUALIZATION")
    print("="*60)
    visualize_solution([1, 2, 3, 4])

    print("\n" + "="*50)
    print("Another example with zeros:")
    visualize_solution([2, 0, 3, 4])


if __name__ == "__main__":
    test_product_except_self()
    run_visualization()

    print("\n" + "="*60)
    analyze_complexity()

"""
Personal Reflection:
- Time to solve: ___ minutes
- Difficulty rating (1-5): ___/5
- What I learned: Prefix/postfix technique and space optimization
- Mistakes made:
- Key insight: Can use result array for both prefix and postfix calculations

Your Code Excellence:
1. **Optimal Algorithm:** O(n) time, O(1) extra space - perfect!
   
2. **Space Optimization Genius:**
   - Uses result array for prefix storage
   - Multiplies by postfix in second pass
   - No extra arrays needed
   
3. **Clean Implementation:**
   - Clear variable names (prefix, postfix)
   - Logical two-pass structure
   - Handles all edge cases naturally

4. **Mathematical Insight:**
   - answer[i] = prefix[i] × postfix[i]
   - Avoids division completely
   - Naturally handles zeros

Algorithm Breakdown:
Pass 1: res[i] = product of nums[0] to nums[i-1]
Pass 2: res[i] *= product of nums[i+1] to nums[n-1]
Result: res[i] = product of all elements except nums[i]

Why Your Approach Rocks:
- Meets all problem constraints perfectly
- Optimal complexity - can't do better
- Elegant use of single result array
- Clear logical progression
- Interview-perfect solution

Code Quality: 10/10
This is the textbook optimal solution that interviewers expect!

Similar Problems to Practice:
- Maximum Product Subarray
- Trapping Rain Water (prefix/suffix technique)
- Candy (bidirectional pass approach)

Interview Notes:
- Explain the prefix/postfix concept clearly
- Walk through the two-pass logic step by step
- Mention space optimization (using result array)
- Discuss why division approach has issues (zeros, precision)
- Show understanding of the mathematical insight
"""