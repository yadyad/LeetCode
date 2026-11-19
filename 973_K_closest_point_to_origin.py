import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = x*x+y*y
            if len(min_heap) < k:
                heapq.heappush(min_heap, (-dist, point))
            else:
                dist_max,point_max = heapq.heappop(min_heap)
                dist_max = -dist_max
                if dist < dist_max:
                    heapq.heappush(min_heap, (-dist, point))
                else:
                    heapq.heappush(min_heap, (-dist_max, point_max))
        a_values, b_values = zip(*min_heap)
        return b_values

s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]],2))
