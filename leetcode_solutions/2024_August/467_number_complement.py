class Solution:
    def findComplement(self, num: int) -> int:
        l = num.bit_length()
        maska = (1 << l) - 1
        return num ^ maska
    

# Example 1:

# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2:

# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


