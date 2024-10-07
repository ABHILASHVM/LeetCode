class Solution:
    def minLength(self, s: str) -> int:
        i=0
        while i<len(s)-1:
            if s[i]+s[i+1]=="AB" or s[i]+s[i+1]=="CD":
                s=s[:i]+s[i+2:]
                i-=1
                i=max(0,i)
            else:
                i+=1
        return len(s)