class Solution:
    def compressedString(self, word: str) -> str:
        result=""
        i=0
        s=set(list(word))
        print(s)
        count=0
        # for j in s:
        while i<len(word)-1:
            if word[i]==word[i+1]:
                count+=1
                i+=1
                if count==9:
                    result=result+"9"+word[i]
                    count=0
            else:
                result=result+str(count+1)+word[i]
                i+=1
                count=0
                
        result+=str(count+1)+word[i]
        return result