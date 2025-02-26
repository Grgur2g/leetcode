class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        final = []
        spaces = set(spaces)
        for i,c in enumerate(s):
            if i in spaces:
                final.append(" ")
                spaces.remove(i)
            final.append(c)
        return "".join(final)
    

# Example 1:

# Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
# Output: "Leetcode Helps Me Learn"
# Explanation: 
# The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
# We then place spaces before those characters.

# Example 2:

# Input: s = "icodeinpython", spaces = [1,5,7,9]
# Output: "i code in py thon"
# Explanation:
# The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
# We then place spaces before those characters.

# Example 3:

# Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
# Output: " s p a c i n g"
# Explanation:
# We are also able to place spaces before the first character of the string.
