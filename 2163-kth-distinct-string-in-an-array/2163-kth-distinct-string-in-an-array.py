class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a={}
        for i in range(len(arr)):
            if arr[i] not in a:
                a[arr[i]]=1
            else:
                a[arr[i]]+=1
        j=0
        for i in a:
            if a[i]==1:
                j+=1
            if j==k:
                return i
        return ""