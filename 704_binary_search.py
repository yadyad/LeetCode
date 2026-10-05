class Solution:
    def binary_search(self, nums,target,start, end):
        mid = start + (end - start)//2
        if start<=end:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
                return self.binary_search(nums, target, start, end)
            else:
                start = mid+1
                return self.binary_search(nums, target, start, end)
        else:
            return -1


    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        return self.binary_search(nums, target, start, end)
s = Solution()
print(s.search(nums=[-1,0,3,5,9,12], target=9))