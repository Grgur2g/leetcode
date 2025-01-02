class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        maxi = -1
        index = -1
        index2 = -1
        for i in range(len(num)):
            if index > -1:
                break
            for j in range(len(num)-1,i,-1):
                if int(num[i]) < int(num[j]):
                    if maxi < int(num[j]):
                        maxi = int(num[j])
                        index = j
                        index2 = i
        num = list(num)
        curr = num[index]
        num[index] = num[index2]
        num[index2] = curr
        num = "".join(num)
        return int(num)
 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
