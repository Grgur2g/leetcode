class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        for i, s in enumerate(sentence):
            if s.startswith(searchWord):
                return i+1
        return -1


# Example 1:

# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

# Example 2:

# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.

# Example 3:

# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.