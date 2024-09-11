class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=bin(start)[2:]
        b=bin(goal)[2:]
        lena=len(a)
        lenb=len(b)
        count=0
        if lena<lenb:
            a="0"*(lenb-lena)+a
        else:
            b="0"*(lena-lenb)+b
        # print(a,b)
        for i in range(len(a)):
            # print(i,count,len(a))
            if a[i]!=b[i]:
                count+=1
            
        return count