import copy


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        candidates.sort()
        temp = candidates

        def dfs(cur, sum, temp):
            if target == sum:
                res.update(copy.deepcopy(cur))
                return
            if target < sum:
                return
            prev = -1
            for j in range(len(temp)):
                if temp[j]==prev:
                    continue
                cur.append(temp[j])
                popped = temp.pop(j)
                dfs(cur, sum+popped,temp)
                temp.insert(j,popped)
                cur.pop()
                prev = temp[j]

        dfs([],0,temp)
        return res



S = Solution()
print(S.combinationSum2([10,1,2,7,6,1,5],8))




