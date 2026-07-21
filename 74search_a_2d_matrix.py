from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix)
        col_length = len(matrix[0])
        start = 0
        end = row_length-1
        while start <= end:
            mid = int((end + start) / 2)
            if matrix[mid][0] > target:
                end = mid - 1
            if matrix[mid][0] < target:
                if binary_search(matrix[mid], target):
                    return True
                else:
                    start = mid + 1
        return False

def binary_search(list: List[int], target: int):
    if len(list) == 1:
        if list[0] == target:
            return True
        else:
            return False
    start = 0
    end = len(list)-1
    while start <= end:
        mid = int((end + start) / 2)
        if list[mid] == target:
            return True
        elif list[mid] > target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1

    return False


s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(matrix, 13))
