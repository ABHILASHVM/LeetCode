# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         # xor=0
#         # lst=[]
#         # for i in queries:
#         #     for j in range(i[0],i[1]+1):
#         #         xor=xor^arr[j]
#         #     lst.append(xor)
#         #     xor=0
#         # return lst
class Solution(object):
    def xorQueries(self, arr, queries):
        n = len(arr)
        pre = [0] * n
        pre[0] = arr[0]
        
        # Compute prefix XOR array
        for i in range(1, n):
            pre[i] = pre[i - 1] ^ arr[i]
        
        res = []
        
        # Answer each query
        for left, right in queries:
            if left == 0:
                res.append(pre[right])
            else:
                res.append(pre[right] ^ pre[left - 1])
        
        return res
        