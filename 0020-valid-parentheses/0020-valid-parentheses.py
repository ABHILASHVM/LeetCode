class Solution:
    def isValid(self, s: str) -> bool:
        # lst=["(",")","{","}","[","]"]
        # a=list(s)
        # while(True):
        #      if a[0] == lst[0]:
        #         if ")" in a:
        #             a.remove("(")
        #             a.remove(")")
        #         else:
        #             return False
        #      elif a[0] == lst[2]:
        #         if "}" in a:
        #             a.remove("{")
        #             a.remove("}")
        #         else:
        #             return False
        #      elif a[0] == lst[4]:
        #         if "]" in a:
        #             a.remove("[")
        #             a.remove("]")
        #         else:
        #             return False
        #      else:
        #         return False
        #      if len(a)==0:
        #         return True
        if len(s)%2 == 1:
            return False
        else:
            stack=[]
            for i in s:
                if i in list("({["):
                    stack.append(i)
                else:

                    if len(stack)!=0 and i == ")" and stack[-1]=="(" :
                        stack.pop(-1)
                    elif len(stack)!=0 and i == "}" and stack[-1]=="{" :
                        stack.pop(-1)
                    elif len(stack)!=0 and i == "]" and stack[-1]=="[":
                        stack.pop(-1)
                    else:
                        return False
            if len(stack)== 0:
                return True
            else: 
                return False