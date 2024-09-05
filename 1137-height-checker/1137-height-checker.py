class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=heights[:]
        heights.sort()
        count=0
        for i in range(len(a)):
            if a[i]!=heights[i]:
                count+=1
        return count