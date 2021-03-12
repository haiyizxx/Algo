#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    # [[2]                [2]
    #  [3, 4]             [5, 6]
    #  [6, 5, 7]          [11, 10, 11]
    #  [4, 1, 8, 3]]      [16, 11, 18, 14]

    # No additional array
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        # f[i][j] = minTotalOf(i, j)
        # f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i-1][j-1] (triangle start from 1)

        for r in range(1, row):
            for c in range(0, r+1):

                # if (r == 1 and c == 1):
                #     continue

                if (c == 0):
                    triangle[r][c] += triangle[r-1][c]

                elif c == r:
                    triangle[r][c] += triangle[r-1][c-1]

                else:
                    triangle[r][c] += min(triangle[r-1][c], triangle[r-1][c-1])

        return min(triangle[-1])

    # 2 row f array
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        # f[i][j] = minTotalOf(i, j)
        # f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i-1][j-1] (triangle start from 1)
        # We actually only need 2 row
        f = [[float('inf')] * (row+1) for _ in range(2)]
        for r in range(1, row+1):
            for c in range(1, r+1):
                f[1][c] = triangle[r-1][c-1]

                if (r == 1 and c == 1):
                    continue

                if (c == 1):
                    f[1][c] += f[0][c]

                elif c == r:
                    f[1][c] += f[0][c-1]

                else:
                    f[1][c] += min(f[0][c], f[0][c-1])
            f[0] = f[1]
            f[1] = [float('inf')] * (row+1)
        return min(f[0])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        # f[i][j] = minTotalOf(i, j)
        # f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i-1][j-1] (triangle start from 1)
        f = [[float('inf')] * (row+1) for _ in range(row+1)]
        for r in range(1, row+1):
            for c in range(1, r+1):
                f[r][c] = triangle[r-1][c-1]

                if (r == 1 and c == 1):
                    continue

                if (c == 1):
                    f[r][c] += f[r-1][c]

                elif c == r:
                    f[r][c] += f[r-1][c-1]

                else:
                    f[r][c] += min(f[r-1][c], f[r-1][c-1])
        return min(f[-1])


# @lc code=end
