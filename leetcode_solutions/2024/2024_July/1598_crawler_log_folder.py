class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for l in logs:
            if l == "../" and counter > 0:
                counter-=1
            elif l != "./" and l != "../":
                counter+=1
        return counter
    


# Example 1:

# Input: logs = ["d1/","d2/","../","d21/","./"]
# Output: 2
# Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

# Example 2:

# Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
# Output: 3

# Example 3:

# Input: logs = ["d1/","../","../","../"]
# Output: 0
