class Solution(object):
    def maxDistance(self, arrays):
        mini = arrays[0][0]
        maxi = arrays[0][-1]
        max_distance = 0

        for arr in arrays[1:]:
            max_distance = max(max_distance, abs(maxi-arr[0]), abs(mini-arr[-1]))
            maxi = max(maxi, arr[-1])
            mini = min(mini, arr[0])

        return max_distance
    


# Example 1:

# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

# Example 2:

# Input: arrays = [[1],[1]]
# Output: 0
