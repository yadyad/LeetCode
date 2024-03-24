class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1

        length = len(nums)
        i = 0
        while i < len(nums):
            if 0 < nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                print(nums[i])
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
            else:
                i += 1
        print(nums)
        for i,val in enumerate(nums):
            if val-1 != i:
                return i+1
        return len(nums)+1




S = Solution()
print(S.firstMissingPositive([7,8,9,11,12]))
