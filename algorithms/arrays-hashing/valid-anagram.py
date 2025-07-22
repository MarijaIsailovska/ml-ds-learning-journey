"""
Problem: Valid Anagram
Source: LeetCode #242
Difficulty: Easy
Date Solved: 2024-07-23

Problem Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Approach:
Sort both strings and compare them. If they're equal after sorting, they contain
the same characters in the same frequencies, making them anagrams.

Time Complexity: O(n log n) - due to sorting both strings
Space Complexity: O(1) if sorting is in-place, O(n) for the sorted strings

Key Insights:
- Anagrams have identical character frequencies
- Sorting reveals the canonical form of character arrangement
- Simple and intuitive approach
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams using sorting approach.

        Args:
            s: str - first string
            t: str - second string

        Returns:
            bool - True if t is anagram of s, False otherwise
        """
        # Sort both strings to get canonical character order
        s = sorted(s)
        t = sorted(t)

        # Compare sorted strings
        if s == t:
            return True
        else:
            return False

    # Optimized version of the same logic
    def isAnagramOptimized(self, s: str, t: str) -> bool:
        """
        More concise version of the same approach.
        """
        return sorted(s) == sorted(t)


# Alternative approaches for comparison
class AlternativeSolutions:
    def isAnagramHashMap(self, s: str, t: str) -> bool:
        """
        Hash map approach - O(n) time, O(1) space (at most 26 characters)
        """
        if len(s) != len(t):
            return False

        char_count = {}

        # Count characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Subtract characters in t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]

        return len(char_count) == 0

    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        Using collections.Counter for frequency comparison
        """
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagramArray(self, s: str, t: str) -> bool:
        """
        Array approach for lowercase letters only - O(n) time, O(1) space
        """
        if len(s) != len(t):
            return False

        # Array to count frequency of each letter (a-z)
        char_count = [0] * 26

        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1

        return all(count == 0 for count in char_count)


# Test cases
def test_is_anagram():
    solution = Solution()

    # Test case 1: Basic anagram
    s1, t1 = "anagram", "nagaram"
    result1 = solution.isAnagram(s1, t1)
    expected1 = True
    assert result1 == expected1, f"Test 1 failed: got {result1}, expected {expected1}"

    # Test case 2: Not anagrams
    s2, t2 = "rat", "car"
    result2 = solution.isAnagram(s2, t2)
    expected2 = False
    assert result2 == expected2, f"Test 2 failed: got {result2}, expected {expected2}"

    # Test case 3: Empty strings
    s3, t3 = "", ""
    result3 = solution.isAnagram(s3, t3)
    expected3 = True
    assert result3 == expected3, f"Test 3 failed: got {result3}, expected {expected3}"

    # Test case 4: Different lengths
    s4, t4 = "a", "ab"
    result4 = solution.isAnagram(s4, t4)
    expected4 = False
    assert result4 == expected4, f"Test 4 failed: got {result4}, expected {expected4}"

    # Test case 5: Same string
    s5, t5 = "listen", "listen"
    result5 = solution.isAnagram(s5, t5)
    expected5 = True
    assert result5 == expected5, f"Test 5 failed: got {result5}, expected {expected5}"

    # Test case 6: One character difference
    s6, t6 = "ac", "bb"
    result6 = solution.isAnagram(s6, t6)
    expected6 = False
    assert result6 == expected6, f"Test 6 failed: got {result6}, expected {expected6}"

    # Test case 7: Repeated characters
    s7, t7 = "aab", "aba"
    result7 = solution.isAnagram(s7, t7)
    expected7 = True
    assert result7 == expected7, f"Test 7 failed: got {result7}, expected {expected7}"

    print("All test cases passed! ✅")


# Benchmark different approaches
def benchmark_approaches():
    """
    Compare performance of different approaches
    """
    import time

    solution = Solution()
    alt = AlternativeSolutions()

    # Test data
    s = "thequickbrownfoxjumpsoverthelazydog" * 100
    t = "godyzalehtrevosjumpxofnworbkceuqiht" * 100

    approaches = [
        ("Sorting", solution.isAnagram),
        ("Hash Map", alt.isAnagramHashMap),
        ("Counter", alt.isAnagramCounter),
        ("Array", alt.isAnagramArray)
    ]

    for name, func in approaches:
        start = time.time()
        for _ in range(1000):
            func(s, t)
        end = time.time()
        print(f"{name}: {(end - start) * 1000:.2f}ms")


if __name__ == "__main__":
    test_is_anagram()
    print("\nBenchmark results:")
    benchmark_approaches()

"""
Personal Reflection:
- Time to solve: ___ minutes
- Difficulty rating (1-5): ___/5
- What I learned: Sorting approach is intuitive but not most efficient
- Mistakes made: 
- Key insight: Multiple ways to solve - sorting vs frequency counting

Approach Comparison:
1. **Sorting (Your approach):**
   - Pros: Simple, intuitive, works with any characters
   - Cons: O(n log n) time complexity
   
2. **Hash Map:**
   - Pros: O(n) time, general solution
   - Cons: More complex code
   
3. **Array counting:**
   - Pros: O(n) time, O(1) space, fastest for lowercase letters
   - Cons: Limited to specific character set

Similar Problems to Practice:
- Group Anagrams (categorize multiple strings)
- Find All Anagrams in a String (substring anagrams)
- Minimum Window Substring (character frequency matching)

Interview Notes:
- Ask about constraints: character set (lowercase only?), string length
- Discuss trade-offs: time vs space, simplicity vs efficiency
- Mention multiple approaches and when to use each
- Consider follow-up: what if strings are very long? (sorting might be better due to space)
"""