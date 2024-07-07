class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        arr1 = [int(x) for x in version1]
        version2 = version2.split(".")
        arr2 = [int(x) for x in version2]

        max_len = max(len(arr1),len(arr2))

        arr1 = arr1 + [0] * (max_len-len(arr1))
        arr2 = arr2 + [0] * (max_len-len(arr2))
        
        for i in range(max_len):
            if arr1[i] > arr2[i]:
                return 1
            elif arr1[i] < arr2[i]:
                return -1
        return 0
    
# Example 1:

# Input: version1 = "1.2", version2 = "1.10"

# Output: -1

# Explanation:

# version1's second revision is "2" and version2's _second revision is "10": 2 < 10, so version1 < version2.

# Example 2:

# Input: version1 = "1.01", version2 = "1.001"

# Output: 0

# Explanation:

# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

# Example 3:

# Input: version1 = "1.0", version2 = "1.0.0.0"

# Output: 0

# Explanation:

# version1 has less revisions, which means every missing revision are treated as "0".
