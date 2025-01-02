class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mapa = [0] * 100001

        for n in nums:
            mapa[n+50000] += 1
        
        k = 0
        for i in range(100001):
            for j in range(mapa[i]):
                nums[k] = i - 50000
                k += 1
        return nums
    


# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         mapa = [0] * 100001

#         for n in nums:
#             mapa[n+50000] += 1
        
#         k = 0
#         for i in range(100001):
#             for j in range(mapa[i]):
#                 nums[k] = i - 50000
#                 k += 1
#         return nums