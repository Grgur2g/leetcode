class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        fix = [0]
        suma = 0
        vow = {'a', 'e', 'i', 'o', 'u'}
        for s in words:
            if s[0] in vow and s[-1] in vow:
                suma += 1
            fix.append(suma)
        
        return [fix[b+1]-fix[a] for a, b in queries]
    

# Example 1:

# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].

# Example 2:

# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# Explanation: Every string satisfies the conditions, so we return [3,2,1].    
