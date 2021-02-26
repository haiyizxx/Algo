#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = [[0] * col for _ in range(row)]
        res[0][0] = grid[0][0]
        for i in range(1, col):
            res[0][i] = grid[0][i] + res[0][i-1]
        for i in range(1, row):
            res[i][0] = res[i-1][0] + grid[i][0]

        for r in range(1, row):
            for c in range(1, col):
                res[r][c] = min(grid[r][c] + res[r-1][c],
                                grid[r][c]+res[r][c-1])

        return res[-1][-1]
# @lc code=end
