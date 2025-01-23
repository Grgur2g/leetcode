class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            suma = sum(grid[i])
            if suma > 1:
                cnt += suma
            elif suma == 1:
                ind = grid[i].index(1)
                if sum(grid[a][ind] for a in range(len(grid))) > 1:
                    cnt += 1
                    
        return cnt


# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

# Example 2:

# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.

# Example 3:

# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
