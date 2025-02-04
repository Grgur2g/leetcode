class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                arr.append(maxi2[-1]+nums[i])
            else:
                arr.append(nums[i])
        return max(arr)


# Example 1:

# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

# Example 2:

# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

# Example 3:

# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
