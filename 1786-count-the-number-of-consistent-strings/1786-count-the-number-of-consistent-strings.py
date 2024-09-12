class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            for j in range(len(i)):
                if i[j] in allowed:
                    flag=1
                else:
                    flag=0
                    break
            if flag:
                count+=1
        return count