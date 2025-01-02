class Solution:
    def compressedString(self, word: str) -> str:
        s = ""
        prev = word[0]
        counter = 1
        for c in word[1:]:
            if counter == 9 or c != prev:
                s+= str(counter) + prev
                counter = 0
                prev = c
            counter+=1

        s+= str(counter) + prev   
        return s




# Example 1:

# Input: word = "abcde"

# Output: "1a1b1c1d1e"

# Explanation:

# Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

# For each prefix, append "1" followed by the character to comp.

# Example 2:

# Input: word = "aaaaaaaaaaaaaabb"

# Output: "9a5a2b"

# Explanation:

# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

#     For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
#     For prefix "aaaaa", append "5" followed by "a" to comp.
#     For prefix "bb", append "2" followed by "b" to comp.

