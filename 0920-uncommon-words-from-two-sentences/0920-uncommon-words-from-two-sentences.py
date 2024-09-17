class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1+" "+s2
        s1=s1.split()
        res=[]
        for i in s1:
            if s1.count(i)==1 and i not in res:
                res.append(i)
        return res
