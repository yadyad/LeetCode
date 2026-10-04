from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0,0
        sum = 0
        res = float('inf')
        for num in nums:
            if num>target:
                return 1
        for right in range(0, len(nums)):
            sum += nums[right]
            while sum > target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
        return res if res != float('inf') else -1

s = Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
