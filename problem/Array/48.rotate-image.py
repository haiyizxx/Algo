#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1 flip row in reverse order
        top, down = 0, len(matrix) - 1
        while top < down:
            temp = matrix[top]
            matrix[top] = matrix[down]
            matrix[down] = temp
            top += 1
            down -= 1

        # Step 2 flip (i,j) -> (j, i)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

# @lc code=end
