class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        st=''
        for i in s:
            if i==')':
                while stack[-1]!='(':
                    st+=stack.pop()
                stack.pop()
                stack.extend(list(st))
                st=''
            else:
                stack.append(i)
        return ''.join(stack)