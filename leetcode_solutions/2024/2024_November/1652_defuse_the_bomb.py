class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        code.extend(code)

        niz = []
        for i in range(n):
            if k > 0:
                niz.append(sum(code[i + 1:i + k + 1]))
            else:
                niz.append(sum(code[i + n + k:i + n]))
        
        return niz
    

# Example 1:

# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. 
# The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

# Example 2:

# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 

# Example 3:

# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. 
# If k is negative, the sum is of the previous numbers.
