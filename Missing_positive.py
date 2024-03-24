from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        largest = -1
        smallest = nums[0]
        for i in nums:
            if(i>largest and i>0):
                largest = i
            elif(i<smallest and i>0):
                smallest = i
        