class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote="".join(sorted(ransomNote))
        magazine=sorted(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine.remove(ransomNote[i])
            else:
                return False
        return True