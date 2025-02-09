class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]-i
            
        def nth_triangle_number(n):
            return n * (n + 1) // 2
        maxi = nth_triangle_number(len(nums))

        from collections import Counter
        c = Counter(nums)

        for k,v in c.items():
            maxi -= nth_triangle_number(v)

        return maxi
    
# Example 1:

# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.

# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 0
# Explanation: There are no bad pairs.
