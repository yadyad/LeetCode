from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        new_list = [intervals.pop(0)]
        while len(intervals) != 0:
            last = new_list.pop()
            current = intervals.pop(0)
            if last[1] >= current[0]:
                if last[1] > current[1]:
                    new_list.append([last[0],last[1]])
                else:
                    new_list.append([last[0],current[1]])
            else:
                new_list.append(last)
                new_list.append(current)
        return new_list








sol = Solution()
a = sol.merge([[1,4],[2,3]])
print(a)
