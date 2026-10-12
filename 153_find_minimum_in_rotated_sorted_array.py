class Solution:


    def findMin(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l = 0
        r = len(nums)-1
        smallest = nums[0]
        while l<=r:

            mid = l + (r-l)//2
            if nums[mid]<smallest:
                smallest = nums[mid]
                r = mid-1
            else:
                l = mid+1
            print(f"l={l}, r={r}, smallest={smallest}")
        return smallest

s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))