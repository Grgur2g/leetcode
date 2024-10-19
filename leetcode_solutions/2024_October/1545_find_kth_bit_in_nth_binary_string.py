class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        def invert(x):
            x = x.replace("0","3")
            x = x.replace("1","0")
            x = x.replace("3","1")
            return x

        def reverse(x):
            x = invert(x)
            return x[::-1]
        
        for iteration in range(n):
            s = s + "1" + reverse(s)
        
        return s[k-1]
    

# Example 1:

# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1st bit is "0".

# Example 2:

# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11th bit is "1".
