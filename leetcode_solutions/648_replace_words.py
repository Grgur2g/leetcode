class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        array = sentence.split(" ")
        solution = []
        to_remove = set()

        for it in dictionary:
            for it2 in dictionary:
                if it.startswith(it2) and it != it2:
                    to_remove.add(it)
                    break

        dictionary = [item for item in dictionary if item not in to_remove]
        for item in array:
            for root in dictionary:
                if item.startswith(root):
                    solution.append(root)
                    break
            else:
                solution.append(item)
        return " ".join(solution)
    

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
