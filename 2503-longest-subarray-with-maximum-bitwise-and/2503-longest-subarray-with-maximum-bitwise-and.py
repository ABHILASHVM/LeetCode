# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         maxxi=max(nums)
#         count=0
#         for i in range(len(nums)):
#             if nums[i]==maxxi:
#                 count+=1
#                 save=i
#                 break
#         if save+1 != len(nums):
#             for i in range(save+1,len(nums)):
#                 if nums[i]==maxxi:
#                     count+=1
#                 else:
#                     break
#         return  count
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxBitwiseAnd = max(nums)
        maxi = 1
        count = 0
        i = 0
        
        while i < len(nums):
            if nums[i] == maxBitwiseAnd:
                while i < len(nums) and nums[i] == maxBitwiseAnd:
                    count += 1
                    i += 1
                maxi = max(maxi, count)
                count = 0
            else:
                i += 1
        
        return maxi