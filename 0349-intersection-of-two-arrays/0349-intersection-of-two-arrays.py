class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            mini=nums2[:]
            maxi=nums1[:]
        else:
            mini=nums1[:]
            maxi=nums2[:]
        res=[]
        for i in mini:
            if i in maxi and i not in res:
                res.append(i)
        return res
        