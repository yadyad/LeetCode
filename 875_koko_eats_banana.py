import math

class Solution:
    def calculate_viable(self, nums, mid,h):
        sum = 0
        for value in nums:
            sum += math.ceil(value/mid)
            if sum > h:
                return False
        if sum <= h:
            return True
        else:
            return False


    def binary_search_left(self, nums, target, start, stop, h):
        print(f"binary_search_left: start={start}, stop={stop}")
        if start>=stop:
            cal =self.calculate_viable(nums,start, h)
            print(cal,start, stop)
            if cal:
                return start
            else:
                return -1
        mid = start + (stop - start) // 2

        if self.calculate_viable(nums,mid,h):
            res = self.binary_search_left(nums, target, start, mid-1, h)
            if res == -1:
                return mid
            else:
                return res
        else:
            res = self.binary_search_left(nums, target, mid+1, stop, h)
            return res



    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start = 1
        stop = -1
        for pile in piles:
            stop = max(pile, stop)
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        return self.binary_search_left(piles, 0, start, stop, h)



s=Solution()
print(s.minEatingSpeed([2,2],h=4))