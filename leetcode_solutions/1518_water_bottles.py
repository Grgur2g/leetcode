class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        prazno = 0
        popijeno = 0
        while numBottles:
            numBottles -= 1
            prazno +=1
            popijeno +=1
            if prazno == numExchange:
                prazno = 0
                numBottles += 1
        return popijeno


# Example 1:

# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.

# Example 2:

# Input: numBottles = 15, numExchange = 4
# Output: 19
# Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
# Number of water bottles you can drink: 15 + 3 + 1 = 19.