## brute force
from collections import Counter
from itertools import product
from typing import List


class Solution1:
    def check_block_size(self,i:int,j:int, cordinates):
        count = 0
        if [i,j] in cordinates:
            count+=1
        if [i,j+1] in cordinates:
            count+=1
        if [i+1,j] in cordinates:
            count+=1
        if [i+1,j+1] in cordinates:
            count+=1
        return count
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        result = [0,0,0,0,0]
        for i in range(0,m-1):
            for j in range(0,n-1):
                index = self.check_block_size(i,j,coordinates)
                result[index]+=1
        return result

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        cnt = Counter()
        res = [(n - 1) * (m - 1), 0, 0, 0, 0]
        for i, j in coordinates:
            for i, j in product([i, i + 1], [j, j + 1]):
                res[cnt[i, j]] -= 1
                cnt[i, j] += 0 < i < m and 0 < j < n
                res[cnt[i, j]] += 1
        return res