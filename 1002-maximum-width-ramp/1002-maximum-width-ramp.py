# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         i=0
#         j=len(nums)-1
#         while i<j:
#             if nums[i]<=nums[j]:
#                 return j-i
#             else:
#                 i+=1
#         return 0
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        # Step 1: Build a decreasing stack of indices
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
                # print(stack)
        maxWidth = 0
        
        # Step 2: Traverse from the end and find maximum width ramp
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - stack.pop())
        
        return maxWidth