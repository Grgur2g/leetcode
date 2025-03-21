class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(x) for x in matrix]
        col_max = [max(x) for x in zip(*matrix)]

        return list(set(row_min) & set(col_max))
    

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
