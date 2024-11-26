class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        players = [True] * n

        for win, lose in edges:
            players[lose] = False
        
        rez = [index for index, value in enumerate(players) if value]
        rez = rez[0] if len(rez) == 1 else -1
        return rez
    

# Example 1:

# Input: n = 3, edges = [[0,1],[1,2]]
# Output: 0
# Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.

# Example 2:

# Input: n = 4, edges = [[0,2],[1,3],[1,2]]
# Output: -1
# Explanation: Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.
