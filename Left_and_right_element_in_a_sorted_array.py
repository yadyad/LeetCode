from typing import List,Optional


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start =  nums.index(target) if target in nums else  -1      
       
        if start == -1: return [-1,-1]

        for i in range(start,len(nums)):
            if nums[i] > target:
                end = i-1
                break
            if i == len(nums)-1:
                end = i
                break

        return [start,end]

sol = Solution()
a = sol.searchRange([2,2],2)
print(a)
    

        