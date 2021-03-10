#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    # [1, 3, 2, 1, 3]
    # index stack [0,1] => [0,2] => [3] => [3, 4]
    #              1,3      1,2      1      1  3
    # res           1        2       1        1
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # Mono increase stack
        stack = []
        res = 0
        # e.g [1,2,3,4,5]
        # need add 0 after 5 to do the calculation
        for i in range(len(heights)+1):

            if i == len(heights):
                h = 0
            else:
                h = heights[i]
            print(stack)
            # Current height < current max height in stack
            while (stack and h < heights[stack[-1]]):
                height = heights[stack.pop()]

                if stack:
                    sidx = stack[-1]
                else:
                    sidx = -1

                res = max(res, height * (i - sidx-1))
                print(i, sidx, res)
            stack.append(i)

        return res

# @lc code=end
