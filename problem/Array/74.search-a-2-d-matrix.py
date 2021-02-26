#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        # if col == 1 and row == 1:
        #     return target == matrix[0][0]
        left, right = 0, row * col - 1
        while left <= right:
            mid = left + (right - left) // 2
            # Key
            mid_element = matrix[mid // col][mid % col]
            if target == mid_element:
                return True

            if target < mid_element:
                right = mid - 1
            elif target > mid_element:
                left = mid + 1

        return False
# @lc code=end
