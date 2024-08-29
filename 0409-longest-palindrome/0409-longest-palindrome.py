class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=set(list(s))
        coun=[]
        for i in a:
            coun.append(s.count(i))
        z=0
        eve=0
        # return coun
        for i in coun:
            if i%2==1:
                z=1
                eve=eve+i-1
            else:
                eve+=i
        if z:
            return eve+1
        else:
            return eve