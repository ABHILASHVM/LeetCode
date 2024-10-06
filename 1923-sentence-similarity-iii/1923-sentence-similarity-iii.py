class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        sentence1=sentence1.split()
        sentence2=sentence2.split()
        n1,n2=len(sentence1),len(sentence2)
        if n1<n2:
            sentence1,sentence2=sentence2,sentence1
            n1,n2=len(sentence1),len(sentence2)
        start,end=0,0
        while start<n2 and sentence2[start]==sentence1[start]:
            start+=1
        while end<n2 and sentence2[n2-end-1]==sentence1[n1-end-1]:
            end+=1
        return start+end>=n2