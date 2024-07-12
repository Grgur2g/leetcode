class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack, stack2 = [], []
        suma = 0
        c1, c2 = ("a", "b") if x > y else ("b","a")
        n1, n2 = sorted((x,y))
        
        for c in s:
            if c == c2 and stack and stack[-1] == c1:
                stack.pop()
                suma+=n2
            else:
                stack.append(c)
        
        for c in stack:
            if  c == c1 and stack2 and stack2[-1] == c2:
                stack2.pop()
                suma+=n1
            else:
                stack2.append(c)
        return suma



# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.

# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
