class AllOne:

    def __init__(self):
        self.dic={}

    def inc(self, key: str) -> None:
        if key not in self.dic:
            self.dic[key]=1
        else:
            self.dic[key]=self.dic[key]+1

    def dec(self, key: str) -> None:
        # if key not in dic:
        #     dic[key]=1
        # else:
        if self.dic[key]==1:
            self.dic.pop(key)
        if key in self.dic:
            self.dic[key]=self.dic[key]-1
        
    def getMaxKey(self) -> str:
        if self.dic:
            maxi=max(self.dic.values())
            for keys in self.dic.keys():
                if self.dic[keys]==maxi:
                    return keys
        else:
            return ""

    def getMinKey(self) -> str:
        if self.dic:
            mini=min(self.dic.values())
            for keys in self.dic.keys():
                if self.dic[keys]==mini:
                    return keys
        else:
            return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()