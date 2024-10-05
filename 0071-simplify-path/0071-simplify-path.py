class Solution:
    def simplifyPath(self, path: str) -> str:
        lst=path.split("/")
        stack=[]
        for i in lst:
            if i.isalpha():
                stack.append(i+"/")
            elif i=="..":
                if stack:
                    stack.pop()
            elif i=="...":
                stack.append(i+"/")
            elif i=="" or  i==" " or i==".":
                pass
            else:
                stack.append(i+"/")
        s="".join(stack)

        return "/"+s[:-1]