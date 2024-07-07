class Solution:
    def countHomogenous(self, s: str) -> int:
        counter = 1
        prev = ""
        suma = 0
        for i in s:
            if prev == i:
                counter+=1
            if prev != i:
                counter = 1
            suma += counter
            prev = i
        return suma % (10**9 + 7)
    

    # Example 1:

    # Input: s = "abbcccaa"
    # Output: 13
    # Explanation: The homogenous substrings are listed as below:
    # "a"   appears 3 times.
    # "aa"  appears 1 time.
    # "b"   appears 2 times.
    # "bb"  appears 1 time.
    # "c"   appears 3 times.
    # "cc"  appears 2 times.
    # "ccc" appears 1 time.
    # 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

    # Example 2:

    # Input: s = "xy"
    # Output: 2
    # Explanation: The homogenous substrings are "x" and "y".

    # Example 3:

    # Input: s = "zzzzz"
    # Output: 15
