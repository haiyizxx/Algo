#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res

        row_start, row_end = 0, len(matrix)
        col_start, col_end = 0, len(matrix[0])

        while (row_start < row_end and col_start < col_end):

            # Traverse right
            for i in range(col_start, col_end):
                res.append(matrix[row_start][i])
            row_start += 1

            # Traverse down
            for i in range(row_start, row_end):
                res.append(matrix[i][col_end-1])
            col_end -= 1

            if row_start < row_end:
                # Traverse left
                for i in range(col_end-1, col_start-1, -1):
                    res.append(matrix[row_end-1][i])
            row_end -= 1

            if col_start < col_end:
                # Traverse up
                for i in range(row_end-1, row_start-1, -1):
                    res.append(matrix[i][col_start])
            col_start += 1

        return res

# @lc code=end
