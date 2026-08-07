from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        start = 0
        end = len(nums) - 1
        ans = set()
        while start < end:
            if nums[start]+ nums[end] in nums:
                ans.add([nums[start],nums[end],)

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))