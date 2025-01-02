class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        def check(rows,cols,point):
            if point[0] < 0 or point[0] > rows-1 or point[1] < 0 or point[1] > cols-1: return False
            else: return True

        visited = []
        start = [rStart, cStart]
        visited.append(start[:])

        flag, inc, switch = -1, 0, 0
        corners = [[0, 0], [0, cols-1], [rows-1, 0], [rows-1, cols-1]]

        while True:
            for a in range(4):
                switch ^= 1
                if a & 1 == 0:
                    inc+=1
                    flag *= -1
                for i in range(inc):
                    start[switch] += flag
                    if check(rows,cols, start): 
                        visited.append(start[:])

            if all(corner in visited for corner in corners):
                return visited 
             

# Example 1:

# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

# Example 2:

# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
