class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum=0
        for i in s:
            for j in str(ord(i)-96):
                sum=sum+int(j)
        if k==1:
            return sum
        
        for i in range(1,k):
            a=sum
            sum=0
            for i in str(a):
                sum=sum+int(i)
        return sum