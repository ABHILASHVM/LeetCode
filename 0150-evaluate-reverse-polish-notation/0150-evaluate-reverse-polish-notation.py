class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for i in tokens:
            if i=="+" or i=="-" or i=="/" or i=="*":
                b=int(res.pop())
                a=int(res.pop())
                print(a,b)
                if i=="+":
                    res.append(a+b)
                elif i=="-":
                    res.append(a-b)
                elif i=="/":
                    res.append(a/b)
                elif i=="*":
                    res.append(a*b)
            else:
                res.append(i)
        return int(res[0])