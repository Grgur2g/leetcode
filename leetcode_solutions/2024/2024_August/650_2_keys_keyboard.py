class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        while n > 1:
            for i in range(2,n+1):
                if n % i == 0:
                    steps += i
                    n = n // i
                    break
        return steps


# Example 1:

# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.

# Example 2:

# Input: n = 1
# Output: 0

        