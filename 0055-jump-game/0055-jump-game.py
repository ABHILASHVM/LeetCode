class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums)==1:
#             return True
#         if len(nums)==2 and nums[0]==2:
#             return True

#         # for i in range(len(nums)-1):
            
#         #     if len(nums)==1:
#         #             return True
#         #     elif i+nums[i] == len(nums) -1:
#         #         print(nums[i])
#         #         return True
#         # jump=0
#         i=0
#         while i<len(nums)+1:
#             i+=nums[i]
#             if i==len(nums)-1 or i>=len(nums):
#                 return True
#             if i<len(nums) and nums[i]==0:
#                 return False
#             # elif i>=len(nums):
#             #     return False
        
#         return False