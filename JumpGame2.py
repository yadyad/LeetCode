class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums) - 1
        res = []

        def dfs(jumping, strength, steps):
            if strength == length:
                res.append(steps)
                return
            if strength > length:
                return
            for i in range(jumping, 0, -1):
                if i > length or nums[i]+strength > length:
                    res.append(steps+1)
                    continue
                strength += i
                steps += 1
                dfs(nums[i]+strength, strength, steps)
                strength -= i
                steps -= 1

        dfs(nums[0], 0, 0)
        if len(res) != 0:
            return min(res)
        return 1


S = Solution()
print(S.jump([1,2,3]))
