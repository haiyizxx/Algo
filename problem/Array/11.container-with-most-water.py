#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            if height[left] <= height[right]:
                ht = height[left]
                left += 1
            else:
                ht = height[right]
                right -= 1
            max_area = max(ht * width, max_area)
        return max_area
# @lc code=end

