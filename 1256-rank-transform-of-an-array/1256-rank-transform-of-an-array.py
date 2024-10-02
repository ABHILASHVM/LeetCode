class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic={}
        a=sorted(list(set(arr)))
        j=1
        for i in a:
            dic[i]=j
            j+=1
        for i in range(len(arr)):
            arr[i]=dic[arr[i]]
        return arr

        # a=arr[:]
        # a.sort()
        # ran=[1]
        # org=[]
        # for i in range(1,len(a)):
        #     if a[i]==a[i-1]:
        #         ran.append(ran[-1])
        #     else:
        #         ran.append(ran[-1]+1)
        # for i in range(len(arr)):
        #     for j in range(len(a)):
        #         if arr[i]==a[j]:
        #             org.append(ran[j])
        #             break

        # return org