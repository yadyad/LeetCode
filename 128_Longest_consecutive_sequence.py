from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        largest = 0
        for num in num_set:
            if num-1 not in num_set:
                current = num
                current_streak = 1
                while current + 1 in num_set:
                    current_streak += 1
                    current += 1
                largest = max(largest, current_streak)
        return largest

s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))