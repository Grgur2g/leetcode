class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new_s=""
        for l in s: new_s+= str(ord(l)-96)
        for _ in range(k):
            suma = 0
            for broj in new_s: suma += int(broj)
            new_s = str(suma)
        return suma
    

# Example 1:

# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.

# Example 2:

# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.

# Example 3:

# Input: s = "zbax", k = 2
# Output: 8

 