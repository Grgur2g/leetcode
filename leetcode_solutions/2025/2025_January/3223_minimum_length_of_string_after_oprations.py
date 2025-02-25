class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if c % 2 else 2 for c in Counter(s).values())
    

# Example 1:

# Input: s = "abaacbcbb"

# Output: 5

# Explanation:
# We do the following operations:

#     Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
#     Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".

# Example 2:

# Input: s = "aa"

# Output: 2

# Explanation:
# We cannot perform any operations, so we return the length of the original string.
