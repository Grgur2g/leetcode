class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(rowSum)):
            curr=[]
            for j in range(len(colSum)):
                mini = min(colSum[j],rowSum[i])
                curr.append(mini)
                colSum[j] -= mini
                rowSum[i] -= mini
            arr.append(curr)
        return arr
    

# Example 1:

# Input: rowSum = [3,8], colSum = [4,7]
# Output: [[3,0],
#          [1,7]]
# Explanation: 
# 0th row: 3 + 0 = 3 == rowSum[0]
# 1st row: 1 + 7 = 8 == rowSum[1]
# 0th column: 3 + 1 = 4 == colSum[0]
# 1st column: 0 + 7 = 7 == colSum[1]
# The row and column sums match, and all matrix elements are non-negative.
# Another possible matrix is: [[1,2],
#                              [3,5]]

# Example 2:

# Input: rowSum = [5,7,10], colSum = [8,6,8]
# Output: [[0,5,0],
#          [6,1,0],
#          [2,0,8]]
