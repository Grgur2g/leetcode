class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        arr= []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                arr.append(nums[i]*nums[j])
        from collections import Counter
        cnt = Counter(arr)
        suma = 0
        for key, value in cnt.items():
            curr = 0
            if value >=4:
                curr = value//2
                curr = (curr * (curr-1)) // 2
                curr *= 8
            suma+= curr
            
        return int(suma)
        


# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
