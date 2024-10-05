# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count=0
#         high=0
#         # for i in s2:
#         #     if i in s1:
#         #         count+=1
#         #         if count>high:
#         #             high=count
#         #     else:
#         #         count=0
#         # if high>=len(s1):
#         #     return True
#         # else:
#         #     return False
#         s=list(s1)
#         sdup=s[:]
#         for i in s2:
#             if i in sdup:
#                 sdup.remove(i)
#                 count+=1
#                 if count>high:
#                     high=count
#             else:
#                 count=0
#                 sdup=s[:]
#         if high>=len(s1):
#             return True
#         else:
#             return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2=len(s1), len(s2)
        if n2<n1: return False
        freq1, freq2 = Counter(s1), Counter(s2[0:n1])
        print(freq1,freq2)
        if freq1==freq2: return True
        l,  r = 1, n1
        while r<n2:
            freq2[s2[l-1]]-=1
            freq2[s2[r]]+=1
            if freq1==freq2: return True
            r+=1
            l+=1
        return False
        