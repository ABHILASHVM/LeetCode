# class Solution:
#     def maxUniqueSplit(self, s: str) -> int:
#         lst=[]
#         i=0
#         j=1
#         while i<len(s) and j<=len(s):
#             if s[i:j] not in lst:
#                 lst.append(s[i:j])
#                 i=j
#                 j+=1
#             else:
#                 j+=1
#         print(lst,j,i)
#         if i<len(s)-1:
#             return len(lst)+1
#         return len(lst)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return 0
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, 1 + backtrack(end, seen))
                    seen.remove(substring)
            return max_splits
        return backtrack(0, set())