class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count=0
        for i in range(len(nums1)-1,-1,-1):
            if nums1[i]==0 and count<len(nums2):
                nums1.pop(i)
                count+=1
            else:
                break
        nums1.extend(nums2)
        return nums1.sort()
