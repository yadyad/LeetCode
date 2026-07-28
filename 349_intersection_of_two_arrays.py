from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)< len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        inter = set()
        for i in range (len(smaller)):
            if smaller[i] in larger:
                inter.add(smaller[i])
        return list(inter)
a = [1,2,2,2]
b = [2,2]
s = Solution()
print(s.intersection(a,b))
