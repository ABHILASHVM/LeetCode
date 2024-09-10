class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst=[]
        count=0
        for i in range(len(s)-1):
            lst.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in lst:
                    lst.append(s[j])
                    if j==len(s)-1:
                        if count < len(lst):
                            count = len(lst)
                        lst=[]
                        break
                else:
                    if count < len(lst):
                        count = len(lst)
                    lst=[]
                    break
        if len(s)==1:
            return 1
        return count