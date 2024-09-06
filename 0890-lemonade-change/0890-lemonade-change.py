class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lst=[]
        for i in bills:
            if i==5:
                lst.append(5)
            elif i==10:
                lst.append(10)
                if 5 in lst:
                    lst.remove(5)
                else:
                    return False
            elif i==20:
                lst.append(20)
                if 10 in lst:
                    lst.remove(10)
                    if 5 in lst:
                        lst.remove(5)
                    else:
                        return False
                else:
                    if lst.count(5)>=3:
                        lst.remove(5)
                        lst.remove(5)
                        lst.remove(5)
                    else:
                        return False
        return True
