class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        arr = []
        arr2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                arr.append(s1[i])
                arr2.append(s2[i])
        return set(arr) == set(arr2) and len(arr) < 3


# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
