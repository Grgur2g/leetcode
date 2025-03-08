class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr = blocks[:k].count("W")
        mini = min(k,curr)
        for index in range(k,len(blocks)):
            if blocks[index-k] == "W":
                curr-=1
            if blocks[index] == "W":
                curr+=1
            mini = min(curr,mini)
        return mini
    

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
