class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # a=set(nums)
        # sum=0
        # count=0
        # for i in a:
        #     for j in range(len(nums)):
        #         if nums[j]==i and count<2:
        #             sum=abs(sum-j)
                   
        #             count+=1
                   
        #         if count==2:
        #             if sum<=k:
                        
        #                 return True
        #             else:
        #                 sum=j
        #                 count=1
        #     sum=0
        #     count=0
        # return False
        save={}
        for i in range(len(nums)):
            if nums[i] in save:
                if i-save[nums[i]]<=k:
                    return True
            save[nums[i]]=i
        return False

                                                                                   