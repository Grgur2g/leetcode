class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack_full = list()
        stack_temp = list()
        temp = ""
        for i in s:
            if i == ")":
                while temp != "(":
                    temp = stack_full.pop()
                    if temp != "(":
                        stack_temp.append(temp)
                stack_full.extend(stack_temp)
                stack_temp.clear()
                temp = ""
            else:
                stack_full.append(i)
        return "".join(stack_full)
    


# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"

# Example 2:

# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# Example 3:

# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
