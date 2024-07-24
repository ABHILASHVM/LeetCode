# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         lst=[]
#         product=1
       
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j!=i:
#                     product=product*nums[j]
            
#             lst.append(product)
#             product=1
#         return lst
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer