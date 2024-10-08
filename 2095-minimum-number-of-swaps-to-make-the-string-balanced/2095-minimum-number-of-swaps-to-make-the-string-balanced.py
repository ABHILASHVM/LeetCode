class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=="[":
                stack.append(i)
            else:
                if len(stack)>=1 and stack[-1]=="[":
                    stack.pop()
                else:
                    stack.append("]")
        print(stack)
        count=0
        for i in stack:
            if i=="]":
                count+=1
        return (count+1)//2
