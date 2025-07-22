"""
Problem: Group Anagrams
Source: LeetCode #49
Difficulty: Medium
Date Solved: 2024-07-23

Problem Description:
Given an array of strings strs, group the anagrams together. You can return
the answer in any order. An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase, typically using all the original
letters exactly once.

Approach:
Use sorted string as a key in hash map to group anagrams. Words with the same
sorted characters are anagrams and will have the same key.

Time Complexity: O(n * k log k) where n = number of strings, k = max string length
Space Complexity: O(n * k) for storing all strings and their keys

Key Insights:
- Anagrams have identical sorted character sequences
- defaultdict(list) simplifies grouping logic
- tuple(sorted(word)) creates hashable key for dictionary
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams using sorted string as key.

        Args:
            strs: List[str] - array of strings to group

        Returns:
            List[List[str]] - list of anagram groups
        """
        # Dictionary to group anagrams by their sorted character key
        Map = defaultdict(list)

        for words in strs:
            # Create unique key for anagrams: sorted characters as tuple
            word = tuple(sorted(words))  # tuple is hashable, can be dict key
            Map[word].append(words)  # group anagrams under same key

        # Return all groups as list of lists
        return list(Map.values())

# Test cases
def test_group_anagrams():
    solution = Solution()

    def sort_groups(groups):
        """Helper to sort groups for comparison (order doesn't matter)"""
        return sorted([sorted(group) for group in groups])

    # Test case 1: Basic example
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.groupAnagrams(strs1)
    expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert sort_groups(result1) == sort_groups(expected1), f"Test 1 failed"

    # Test case 2: Empty string
    strs2 = [""]
    result2 = solution.groupAnagrams(strs2)
    expected2 = [[""]]
    assert result2 == expected2, f"Test 2 failed"

    # Test case 3: Single character
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    expected3 = [["a"]]
    assert result3 == expected3, f"Test 3 failed"

    # Test case 4: No anagrams
    strs4 = ["abc", "def", "ghi"]
    result4 = solution.groupAnagrams(strs4)
    assert len(result4) == 3, "Test 4 failed: should have 3 separate groups"
    assert all(len(group) == 1 for group in result4), "Test 4 failed: each group should have 1 element"

    # Test case 5: All same anagrams
    strs5 = ["abc", "bca", "cab"]
    result5 = solution.groupAnagrams(strs5)
    expected5 = [["abc", "bca", "cab"]]
    assert len(result5) == 1, "Test 5 failed: should have 1 group"
    assert len(result5[0]) == 3, "Test 5 failed: group should have 3 elements"

    # Test case 6: Duplicate strings
    strs6 = ["abc", "abc", "bca"]
    result6 = solution.groupAnagrams(strs6)
    assert len(result6) == 1, "Test 6 failed: should have 1 group"
    assert len(result6[0]) == 3, "Test 6 failed: group should have 3 elements"

    print("All test cases passed! ✅")


# Performance comparison
def analyze_approaches():
    """
    Compare different approaches for grouping anagrams
    """
    solution = Solution()


    # Test with longer strings to see time complexity differences
    test_data = [
        "thequickbrownfox", "foxbrownquickthe", "hello", "world",
        "olleh", "dlrow", "anagram", "nagaram", "python", "nohtyp"
    ]

    print("Approach Analysis:")
    print("1. Sorted Key (Your approach):")
    print("   - Time: O(n * k log k)")
    print("   - Space: O(n * k)")
    print("   - Pros: Simple, handles any characters")
    print("   - Cons: Slower for very long strings")

    print("\n2. Character Count Key:")
    print("   - Time: O(n * k)")
    print("   - Space: O(n * k)")
    print("   - Pros: Faster, optimal time complexity")
    print("   - Cons: More complex, assumes lowercase a-z only")

    print("\n3. Your approach is excellent because:")
    print("   - Clean and readable code")
    print("   - Handles any character set (unicode, symbols, etc.)")
    print("   - Good performance for typical string lengths")
    print("   - Uses tuple() smartly for hashable keys")


if __name__ == "__main__":
    test_group_anagrams()
    print("\n" + "=" * 50)
    analyze_approaches()

"""
Personal Reflection:
- Time to solve: _20__ minutes
- Difficulty rating (1-5): _2__/5
- What I learned: Using sorted string as dictionary key for grouping
- Mistakes made: 
- Key insight: tuple(sorted(word)) creates perfect hashable key for anagrams

Your Code Strengths:
1. **Smart Key Choice:** tuple(sorted(words)) is brilliant
   - Tuple is hashable (can be dict key)
   - Sorted string uniquely identifies anagram group

2. **defaultdict Usage:** Eliminates need to check if key exists
   - Cleaner code than regular dict
   - Automatically creates empty list for new keys

3. **Clean Logic:** Simple one-pass solution
   - Easy to understand and maintain
   - Handles all edge cases naturally

Code Quality: 9/10
- Very clean and Pythonic
- Good variable names
- Efficient use of built-in functions

Optimization Opportunities:
- For very long strings: character counting approach is O(n*k) vs your O(n*k log k)
- For lowercase-only: array counting even faster
- But your approach is more general and equally readable

Similar Problems to Practice:
- Valid Anagram (foundation problem)
- Find All Anagrams in a String (sliding window)
- Anagrams in a Dictionary (trie-based approach)

Interview Notes:
- Explain why tuple(sorted()) works as a key
- Discuss time complexity: sorting dominates
- Mention alternative approaches and trade-offs
- Show understanding of hashable vs non-hashable types
- Demonstrate knowledge of defaultdict benefits
"""