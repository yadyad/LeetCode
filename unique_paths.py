class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    table[i][j] == 1
                else:
                    table[i][j] = table[i][j-1] + table[i-1][j]
        print(table)
        return table[m-1][n-1]


S = Solution()
print(S.uniquePaths(3,7))