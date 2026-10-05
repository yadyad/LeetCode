class Solution:


    def binary_search(self, nums: list[int], target: int, start: int, end: int,left: bool) -> None | list[int] | int:
        if start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                if left:
                    index = self.binary_search(nums, target, start, mid-1, left)
                    if index == -1:
                        return mid
                    else:
                        return index
                else:
                    index = self.binary_search(nums, target, mid+1, end, left)
                    if index == -1:
                        return mid
                    else:
                        return index
            elif nums[mid] > target:
                end = mid-1
                return self.binary_search(nums, target, start, end,left)
            else:
                start = mid+1
                return self.binary_search(nums, target, start, end,left)
        else:
            return -1
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = 0
        end = len(nums) - 1
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        left = self.binary_search(nums, target, start, end,True)
        right = self.binary_search(nums, target, start, end,False)
        return [left,right]


s = Solution()
print(s.searchRange([1,2,2],target = 2))
