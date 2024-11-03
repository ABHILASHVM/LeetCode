class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        leng=len(s)
        i=0
        while i<leng:
            k=s[i:]+s[:i]
            if k==goal:
                return True
            i+=1
        return False