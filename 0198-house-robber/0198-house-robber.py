class Solution:
    def rob(self, nums: List[int]) -> int:
        # e,o=0,0
        # for i in range(len(nums)):
        #     if i%2==0:
        #         e+=nums[i]
        #     else:
        #         o+=nums[i]
        # return max(e,o)
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]