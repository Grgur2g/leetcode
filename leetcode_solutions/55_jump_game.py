class Solution:
    def canJump(self, nums: List[int]) -> bool:
        suma = nums[0]
        for i in range(1,len(nums)):
            if not suma: return False
            suma = max(nums[i], suma-1) 
        return True
# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
