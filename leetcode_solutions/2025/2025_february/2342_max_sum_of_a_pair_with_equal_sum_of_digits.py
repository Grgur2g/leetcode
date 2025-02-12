class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calc(num):
            suma = 0
            while num > 0:
                suma+=num%10
                num //= 10
            return suma
        
        c = collections.defaultdict(list)
        [c[calc(num)].append(num) for num in nums]

        maxi = -1
        for _ ,v in c.items():
            if len(v) > 1:
                v.sort()
                maxi = max(maxi,v[-1]+v[-2])

        return maxi
        

# Example 1:

# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.

# Example 2:

# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.
