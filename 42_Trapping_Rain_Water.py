from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = [0 for i in range(len(height))]
        rain = []
        left.append(0)
        for i in range(1,len(height)):
            if height[i-1] > left[i-1]:
                left.append(height[i-1])
            else:
                left.append(left[i-1])
        print(left)
        right[len(right)-1] = 0
        for i in range(len(height)-2, -1, -1):
            if height[i+1]> right[i+1]:
                right[i] = height[i+1]
            else:
                right[i] = right[i+1]
        print(right)
        sum = 0
        for i in range(len(height)):
            temp = max(min(left[i], right[i]) - height[i],0)
            rain.append(temp)
            sum += temp
        return sum





s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))