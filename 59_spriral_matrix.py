from typing import List
import numpy as np


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, up, down = 0, n - 1, 0, n - 1
        matrix = [[0] * n for _ in range(n)]
        count = 1
        row, column = 0, 0
        direction = 1
        flag = 0
        #direction 0 = left, 1= right, 2 = down, 3 = up
        for i in range(n * n):
            matrix[row][column] = count
            count += 1
            if flag != 0:
                if column == right and direction == 1:
                    direction = 2
                    up += 1
                elif row == down and direction == 2:
                    direction = 0
                    right -= 1
                elif column == left and direction == 0:
                    direction = 3
                    down -= 1
                elif row == up and direction == 3:
                    direction = 1
                    left += 1
            else:
                flag = 1
            if direction == 0:
                column -= 1
            elif direction == 1:
                column += 1
            elif direction == 2:
                row += 1
            elif direction == 3:
                row -= 1

        return matrix


sol = Solution()
n = 5
a = sol.generateMatrix(n)

for i in range(n):
    print(a[i])

