"""
Problem: Encode and Decode Strings
Source: LeetCode #271 (Premium) / NeetCode
Difficulty: Medium
Date Solved: 2024-07-23

Problem Description:
Design an algorithm to encode a list of strings to a string. The encoded string
is then sent over the network and is decoded back to the original list of strings.

The encoding/decoding algorithm should handle any possible characters, including
special characters and delimiters.

Approach:
Use a simple delimiter ("|") to separate strings during encoding. During decoding,
split by the delimiter to reconstruct the original list.

Time Complexity:
- Encode: O(n * m) where n = number of strings, m = average string length
- Decode: O(k) where k = total length of encoded string
Space Complexity: O(k) for storing the result

Key Insights:
- Simple delimiter approach works when strings don't contain the delimiter
- Need to handle edge cases like empty strings
- Manual string building and parsing approach
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings into a single string using delimiter.

        Args:
            strs: List[str] - list of strings to encode

        Returns:
            str - encoded string with "|" as delimiter
        """
        string = ""

        # Concatenate each string with delimiter
        for i in range(len(strs)):
            string += strs[i] + "|"

        return string

    def decode(self, s: str) -> List[str]:
        """
        Decode an encoded string back to list of strings.

        Args:
            s: str - encoded string with "|" delimiters

        Returns:
            List[str] - original list of strings
        """
        list = []  # result list
        string = ""  # current string being built
        i = 0

        # Parse through encoded string character by character
        while i < len(s):
            j = i

            # Build current string until delimiter is found
            while s[j] != "|":
                string += s[j]
                j = j + 1
                i = i + 1

            # Add completed string to result
            list.append(string)
            string = ""  # reset for next string
            i = i + 1  # skip the delimiter "|"

        return list


# Alternative approaches for comparison
class AlternativeSolutions:
    def encode_v2(self, strs: List[str]) -> str:
        """
        More Pythonic approach using join
        """
        return "|".join(strs) + "|"

    def decode_v2(self, s: str) -> List[str]:
        """
        Using built-in split method
        """
        if not s:
            return []
        return s.rstrip("|").split("|")

    def encode_length_prefix(self, strs: List[str]) -> str:
        """
        Length-prefixed encoding - handles strings with delimiters
        Format: "length:string" for each string
        """
        result = ""
        for s in strs:
            result += str(len(s)) + ":" + s
        return result

    def decode_length_prefix(self, s: str) -> List[str]:
        """
        Decode length-prefixed strings
        """
        result = []
        i = 0

        while i < len(s):
            # Find the colon separator
            colon_pos = s.find(":", i)

            # Extract length
            length = int(s[i:colon_pos])

            # Extract string of that length
            start = colon_pos + 1
            string = s[start:start + length]
            result.append(string)

            # Move to next string
            i = start + length

        return result


# Test cases
def test_encode_decode():
    solution = Solution()

    # Test case 1: Basic strings
    strs1 = ["hello", "world"]
    encoded1 = solution.encode(strs1)
    decoded1 = solution.decode(encoded1)
    expected1 = ["hello", "world"]
    assert decoded1 == expected1, f"Test 1 failed: got {decoded1}, expected {expected1}"
    print(f"Test 1: {strs1} -> '{encoded1}' -> {decoded1} ✅")

    # Test case 2: Empty string in list
    strs2 = ["", "hello", "", "world", ""]
    encoded2 = solution.encode(strs2)
    decoded2 = solution.decode(encoded2)
    expected2 = ["", "hello", "", "world", ""]
    assert decoded2 == expected2, f"Test 2 failed: got {decoded2}, expected {expected2}"
    print(f"Test 2: {strs2} -> '{encoded2}' -> {decoded2} ✅")

    # Test case 3: Single string
    strs3 = ["lonely"]
    encoded3 = solution.encode(strs3)
    decoded3 = solution.decode(encoded3)
    expected3 = ["lonely"]
    assert decoded3 == expected3, f"Test 3 failed: got {decoded3}, expected {expected3}"
    print(f"Test 3: {strs3} -> '{encoded3}' -> {decoded3} ✅")

    # Test case 4: Empty list
    strs4 = []
    encoded4 = solution.encode(strs4)
    decoded4 = solution.decode(encoded4)
    expected4 = []
    assert decoded4 == expected4, f"Test 4 failed: got {decoded4}, expected {expected4}"
    print(f"Test 4: {strs4} -> '{encoded4}' -> {decoded4} ✅")

    # Test case 5: Special characters (but no pipe)
    strs5 = ["hello@world", "test#123", "a b c"]
    encoded5 = solution.encode(strs5)
    decoded5 = solution.decode(encoded5)
    expected5 = ["hello@world", "test#123", "a b c"]
    assert decoded5 == expected5, f"Test 5 failed: got {decoded5}, expected {expected5}"
    print(f"Test 5: {strs5} -> '{encoded5}' -> {decoded5} ✅")

    print("All test cases passed! ✅")


# Performance comparison
def benchmark_approaches():
    """
    Compare different encoding approaches
    """
    import time

    solution = Solution()
    alt = AlternativeSolutions()

    # Test data
    test_strings = ["string" + str(i) for i in range(1000)]

    print("\nPerformance Comparison:")

    # Test your approach
    start = time.time()
    for _ in range(100):
        encoded = solution.encode(test_strings)
        decoded = solution.decode(encoded)
    end = time.time()
    print(f"Your approach: {(end - start) * 1000:.2f}ms")

    # Test Pythonic approach
    start = time.time()
    for _ in range(100):
        encoded = alt.encode_v2(test_strings)
        decoded = alt.decode_v2(encoded)
    end = time.time()
    print(f"Pythonic approach: {(end - start) * 1000:.2f}ms")


if __name__ == "__main__":
    test_encode_decode()
    benchmark_approaches()

"""
Personal Reflection:
- Time to solve: ___ minutes
- Difficulty rating (1-5): ___/5
- What I learned: String manipulation and parsing techniques
- Mistakes made:
- Key insight: Simple delimiter approach, but need to consider edge cases

Your Code Analysis:
Strengths:
1. **Clear Logic:** Step-by-step manual parsing approach
2. **Understandable:** Easy to follow the encoding/decoding process
3. **Manual Control:** Full control over string building process

Potential Issues:
1. **Delimiter Collision:** If input strings contain "|", it breaks
2. **Efficiency:** Manual string concatenation vs built-in methods
3. **Edge Cases:** Need to handle empty lists, empty strings carefully

Improvements to Consider:
1. **Length-Prefixed Encoding:** Use "length:string" format
2. **Escape Characters:** Escape delimiter if found in strings
3. **Built-in Methods:** Use split/join for cleaner code

Real-World Applications:
- Network protocols
- Data serialization
- CSV parsing
- Message formatting

Similar Problems to Practice:
- Serialize and Deserialize Binary Tree
- Design Compressed String Iterator
- String Compression

Interview Notes:
- Discuss edge cases: what if strings contain delimiter?
- Mention alternative approaches: length-prefixed, escape characters
- Consider trade-offs: simplicity vs robustness
- Show awareness of potential failures in your approach
- Demonstrate ability to improve solution when prompted
"""