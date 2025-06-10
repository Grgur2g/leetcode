class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        a = Counter(s)
        maxn, minp = 0, 101
        for key, value in a.items():
            if value % 2: maxn = max(maxn,value)
            else: minp = min(minp,value)

        return maxn-minp
 

# Example 1:

# Input: s = "aaaaabbc"

# Output: 3

# Explanation:

#     The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
#     The maximum difference is 5 - 2 = 3.

# Example 2:

# Input: s = "abcabcab"

# Output: 1

# Explanation:

#     The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
#     The maximum difference is 3 - 2 = 1.

