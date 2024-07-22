class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        lst=[1,1]
        new=[]
        if numRows==1:
            return [res[0]]
        for i in range(numRows-2):
            new.append(1)
            for j in range(len(lst)-1):
                new.append(lst[j]+lst[j+1])
            new.append(1)
            res.append(new[:])
            lst=new[:]
            new=[]
        return res