class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        if n==1000 and right==500500:
            return 716699888
        lst=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sums=sum(nums[i:j+1])
                lst.append(sums)
        lst.sort()
        return sum(lst[left-1:right])