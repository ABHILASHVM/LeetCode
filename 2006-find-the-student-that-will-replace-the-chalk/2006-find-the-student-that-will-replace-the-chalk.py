class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # if len(chalk)==1:
        #     return 0
        # while True:
        #     for i in range(len(chalk)):
        #         k=k-chalk[i]
        #         if k<0:
        #             return i
        rem=k%sum(chalk)
        for i in range(len(chalk)):
            rem=rem-chalk[i]
            if rem<0:
                return i