class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0
        for c in s:
            if c == "(":
                l += 1
            elif l > 0:
                l-=1
            else:
                r+=1
        return l + r
    

# Example 1:

# Input: s = "())"
# Output: 1

# Example 2:

# Input: s = "((("
# Output: 3