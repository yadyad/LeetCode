from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        stop = len(numbers) - 1

        while start < stop:
            sum = numbers[start] + numbers[stop]
            if sum == target:
                return [start+1, stop+1]
            elif sum < target:
                start += 1
            elif sum > target:
                stop -= 1


s = Solution()
print(s.twoSum([2,7,11,15], 9))