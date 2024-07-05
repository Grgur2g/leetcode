class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while 1:
            sum_ = 0
            for c in str(n):
                sum_ += int(c) ** 2
                
            if sum_ == 1:
                return True
            
            n = sum_
            if n in visited:
                return False
            else:
                visited.append(n)


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:

# Input: n = 2
# Output: false
