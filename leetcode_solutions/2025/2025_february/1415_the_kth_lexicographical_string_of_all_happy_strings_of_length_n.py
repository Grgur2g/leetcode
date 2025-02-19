class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        l = 3 * (2**(n-1))
        if k > l:
            return ""
        if l/3 >= k:
            start = "a"
            left = 0
            right = l/3
        elif l/3*2 >= k:
            start = "b"
            left = l/3 + 1
            right = l/3*2
        else: 
            start = "c"
            left = l/3*2 + 1
            right = l
        for j in range(n-1):
            if start[-1] == "a":
                candy = ["b","c"]
            elif start[-1] == "b":
                candy = ["a","c"]
            else: candy = ["a","b"]
            
            middle = (left+right) / 2
            
            if k > middle:
                left = middle
                start+=candy[-1]
            else:
                right = middle
                start+=candy[-2]
            
        return start
    


# Example 1:

# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

# Example 2:

# Input: n = 1, k = 4
# Output: ""
# Explanation: There are only 3 happy strings of length 1.

# Example 3:

# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
