class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True


# Example 1:

# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32

# Example 2:

# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34

# Example 3:

# Input: n = 21
# Output: false
