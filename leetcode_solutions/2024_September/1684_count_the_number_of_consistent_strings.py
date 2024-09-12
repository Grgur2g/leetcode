class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n = len(words)
        for w in words:
            for l in w:
                if l not in allowed:
                    n-=1
                    break
        return n
    

# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Example 2:

# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:

# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
