import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [i for i in nums[:k]]
        heapq.heapify(heap)
        for i in nums[k:]:
            low = heapq.heappop(heap)
            if i > low:
                heapq.heappush(heap, i)
            else:
                heapq.heappush(heap, low)
        return heapq.heappop(heap)

s = Solution()
print(s.findKthLargest([3,2,1,5,6,6,4], 2))