class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
        # s=self.nums[:]
        # for i in range(self.k+1):
        #     if i==self.k:
        #         return max(s)
        #     s.remove(max(s))


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)