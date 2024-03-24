from typing import List,Optional
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)-1
        i = length
        flag = 0
        while(i>0):
            if(nums[i]>nums[i-1]):
                tempValue = nums[i-1]
                j=i
                smallest_index = -1
                #finding next smallest value that ith pos
                if(j<=length):
                    smallest = abs(nums[i-1]-nums[j])
                    while(j<=length):
                        distence = abs(nums[i-1]-nums[j])
                        if(distence<=smallest and distence != 0 and nums[i-1]<nums[j]):
                            smallest = distence
                            smallest_index = j
                        j+=1
                else:
                    nums[i-1]=nums[i]
                    nums[i]=tempValue
                    print(nums)
                    flag = 1
                    break
                #storing ith smallest value to i-1 position
                nums[i-1] = nums[smallest_index]
                #creating new sorting list for merging
                arr = []
                arr.extend(nums[i:smallest_index])
                if(smallest_index!=length):
                    arr.extend(nums[smallest_index+1:length+1])
                arr.append(tempValue)
                arr.sort()
                print(arr)
                j=i
                k=0
                while(j<=length):
                    nums[j] = arr[k]
                    k+=1
                    j+=1
                print(nums)
                flag = 1
                break
            else:
                i-=1
        if(flag!=1):
            nums.sort()
            print(nums)

sol = Solution()
sol.nextPermutation([8,6,4,9,5,3])