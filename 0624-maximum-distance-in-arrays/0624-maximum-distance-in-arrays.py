class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # mini=999999999999
        # maxi=-99999999999
        # for i in arrays:
        #     if min(i)<mini:
        #         mini=min(i)
        #     if max(i)>maxi:
        #         maxi=max(i)
        # return maxi-mini
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance