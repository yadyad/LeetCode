import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        cooldown = deque()
        timer = 0
        for k, v in freq.items():
            heapq.heappush(heap, -v)

        while heap or cooldown:
            if heap:
                task = -heapq.heappop(heap)
                if task>1:
                    cooldown.append((task-1,timer+n+1))
            timer+=1

            while cooldown and cooldown[0][1] == timer:
                task_count, next_iteration = cooldown[0]
                cooldown.popleft()
                heapq.heappush(heap, -task_count)

        return timer
class Solution2:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        c = Counter(tasks)
        most_freq = max(c.values())
        most_freq_count = list(c.values()).count(most_freq)
        slots = (most_freq - 1) * (n - most_freq_count + 1)
        remaining = len(tasks) - (most_freq * most_freq_count)
        idle = max(0, slots - remaining)
        return len(tasks) + idle

