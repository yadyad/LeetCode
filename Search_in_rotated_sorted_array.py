from typing import List,Optional
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = left + (right-left)//2
        while(left<=right):
            if(nums[mid]>nums[right]):
                left = mid+1
            else:
                right = mid-1
    
        def binarySearch(left_BS,right_BS,target):
            left,right = left_BS,right_BS
            mid = left + (right-left)//2
            while(left<=right):
                if(target == nums[mid]):
                    return mid
                elif(target<nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            return -1
        
        if(a:=binarySearch(0,left-1,target)) != -1:
            return a
        return binarySearch(left,len(nums)-1,target)

            



sol = Solution()
a = sol.search([4,5,6,7,8,0,1,2],0)
print(a)

