class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==1:
                res.append(i)
            if len(res)==2:
                break
        return res