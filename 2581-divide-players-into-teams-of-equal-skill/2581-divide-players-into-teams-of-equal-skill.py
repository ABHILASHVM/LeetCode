class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        sum=0
        chem=skill[0]+skill[-1]
        while i<j:
            if skill[i]+skill[j]==chem:
                sum=sum+(skill[i]*skill[j])
            else:
                return -1
            i+=1
            j-=1
        return sum