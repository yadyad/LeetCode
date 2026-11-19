import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = []
        for x in stones:
            heapq.heappush(max_heap, -x)
        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)
            if a==b:
                continue
            else:
                res = abs(a-b)
                heapq.heappush(max_heap, -res)

        if len(max_heap)==0:
            return 0
        return -heapq.heappop(max_heap)

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
