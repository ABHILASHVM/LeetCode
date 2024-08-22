class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num)[2:]
        # s='1'*(len(a)-1)
        s=""
        for i in a:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)
        # a=int(a)
        # s=int(s)
        # return int(str(a^s),2)