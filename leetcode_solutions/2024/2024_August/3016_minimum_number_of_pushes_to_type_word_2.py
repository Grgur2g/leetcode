class Solution:
    def minimumPushes(self, word: str) -> int:
        curr = Counter(word)
        counter, suma = 0, 0
        for key, value in curr.most_common():
            suma += value*((counter//8) + 1)
            counter+=1
        return suma
    

# Example 1:

# Input: word = "abcde"
# Output: 5
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "a" -> one push on key 2
# "b" -> one push on key 3
# "c" -> one push on key 4
# "d" -> one push on key 5
# "e" -> one push on key 6
# Total cost is 1 + 1 + 1 + 1 + 1 = 5.
# It can be shown that no other mapping can provide a lower cost.

# Example 2:

# Input: word = "xyzxyzxyzxyz"
# Output: 12
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "x" -> one push on key 2
# "y" -> one push on key 3
# "z" -> one push on key 4
# Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
# It can be shown that no other mapping can provide a lower cost.
# Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

# Example 3:

# Input: word = "aabbccddeeffgghhiiiiii"
# Output: 24
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "a" -> one push on key 2
# "b" -> one push on key 3
# "c" -> one push on key 4
# "d" -> one push on key 5
# "e" -> one push on key 6
# "f" -> one push on key 7
# "g" -> one push on key 8
# "h" -> two pushes on key 9
# "i" -> one push on key 9
# Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
# It can be shown that no other mapping can provide a lower cost.
