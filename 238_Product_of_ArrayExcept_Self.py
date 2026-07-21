from sys import prefix
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        result = []
        for i in range(1,len(nums),1):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        print(prefix)
        print(suffix)
        print(result)

##
#can also remove the last iteration by combining with iteration for result
s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))