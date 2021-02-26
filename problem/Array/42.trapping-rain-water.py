#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        ans = 0
        while left < right:
            if left_max <= right_max:
                ans += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])

            else:
                ans += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

        return ans

    def trap2(self, height):
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        ans = 0

        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(height[i], left_max[i-1])
        for i in range(n-1, -1, -1):
            if i == n-1:
                right_max[i] = height[i]
            else:
                right_max[i] = max(height[i], right_max[i+1])

        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans
# @lc code=end
