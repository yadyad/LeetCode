from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        active = True
        for i,val in enumerate(intervals):
            if val[1]>=newInterval[0]:
                intervals.insert(i+1,newInterval)
                active = False
                break
        if active == True:
            intervals.append(newInterval)
        intervals = sorted(intervals)
        new_list = [intervals.pop(0)]
        while len(intervals) != 0:
            last = new_list.pop()
            current = intervals.pop(0)
            if last[1] >= current[0]:
                if last[1] > current[1]:
                    new_list.append([last[0], last[1]])
                else:
                    new_list.append([last[0], current[1]])
            else:
                new_list.append(last)
                new_list.append(current)
        return new_list



sol = Solution()
print(sol.insert([[1, 5]],[6,8]))

