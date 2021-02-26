#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        res = [[0] * col for _ in range(row)]

        for i in range(col):
            if obstacleGrid[0][i] == 1:
                break
            res[0][i] = 1

        for i in range(row):
            if obstacleGrid[i][0] == 1:
                break
            res[i][0] = 1

        for r in range(1, row):
            for c in range(1, col):
                if obstacleGrid[r][c]:
                    res[r][c] = 0
                else:
                    res[r][c] = res[r-1][c] + res[r][c-1]
        return res[-1][-1]

# @lc code=end
