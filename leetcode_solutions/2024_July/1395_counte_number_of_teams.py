class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        for j in range(n):
            less_before = greater_before = less_after = greater_after = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    less_before += 1
                elif rating[i] > rating[j]:
                    greater_before += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_after += 1
                elif rating[k] > rating[j]:
                    greater_after += 1

            teams += less_before * greater_after + greater_before * less_after
        
        return teams


# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

# Example 2:

# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.

# Example 3:

# Input: rating = [1,2,3,4]
# Output: 4
