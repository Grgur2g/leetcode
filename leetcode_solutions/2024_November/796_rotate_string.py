class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for _ in range(len(s)):
            if s == goal:
                return True
            s = s[1::] + s[0]
        return False
        
        
# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
