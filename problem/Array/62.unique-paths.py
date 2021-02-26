#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n for _ in range(m)]
        for i in range(n):
            res[0][i] = 1
        for i in range(m):
            res[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]

# @lc code=end
