class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])**2
        suma = n * (n+1) / 2
        suma2 = 0
        seen = set()
        for arr in grid:
            for a in arr:
                if a in seen:
                    x = a
                else:
                    seen.add(a)
                    suma2 += a
        return [x, int(suma-suma2)]
                

# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

# Example 2:

# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
