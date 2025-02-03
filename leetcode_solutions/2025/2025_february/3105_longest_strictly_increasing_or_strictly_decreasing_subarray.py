class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr = nums[0]
        curr, maxi = 1, 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                curr+=1
                maxi = max(maxi,curr)
            else:
                curr = 1
        curr = 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                curr+=1
                maxi = max(maxi,curr)
            else:
                curr = 1
        return maxi 


# Example 1:
# Input: nums = [1,4,3,3,2]
# Output: 2
# Explanation:
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
# Hence, we return 2.

# Example 2:
# Input: nums = [3,3,3,3]
# Output: 1
# Explanation:
# The strictly increasing subarrays of nums are [3], [3], [3], and [3].
# The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
# Hence, we return 1.

# Example 3:
# Input: nums = [3,2,1]
# Output: 3
# Explanation:
# The strictly increasing subarrays of nums are [3], [2], and [1].
# The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
# Hence, we return 3.
