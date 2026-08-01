from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = {}
        sum = 0
        result = 0
        prefixSumCount[0] = 1
        for i,value in enumerate(nums):
            sum += value
            if sum-k in prefixSumCount.keys():
                result+=prefixSumCount[sum-k]
            prefixSumCount[sum] = prefixSumCount.get(sum, 0) + 1


        return result

s = Solution()
print(s.subarraySum([1,1,1],2))

