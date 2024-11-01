class Solution:
    def makeFancyString(self, s: str) -> str:
        niz = []
        c = 1
        niz.append(s[0])
        for l in s[1::]:
            if niz[-1] == l:
                if c == 2:
                    continue
                else:
                    c+=1
                    niz.append(l)
            else:
                niz.append(l)
                c = 1
        return "".join(niz)
        

# Example 1:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".

# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".

# Example 3:

# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
