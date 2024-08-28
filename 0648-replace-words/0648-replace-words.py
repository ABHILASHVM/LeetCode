class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lst=sentence.split()
        for j in dictionary:
            for i in range(len(lst)):
                if j in lst[i][:len(j)]:
                    lst[i]=j
        return " ".join(lst)