from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            bucket[value].append(key)
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i]:
                result.extend(bucket[i])
                if len(result) >= k:
                    break
        return result

s = Solution()
print(s.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))