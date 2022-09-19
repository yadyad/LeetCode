from typing import List
def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height)-1
    maxLen = min(height[i],height[j])
    maxVolume = maxLen*i-j
    while(i<j):
        maxVolume = max(maxVolume,min(height[i],height[j]*i-j))
        if(height[i]<height[j]):
            i=i+1
        else:
            j = j-1
    return maxVolume
print(maxArea([1,8,6,2,5,4,8,3,7]))