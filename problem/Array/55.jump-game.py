#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = 0
        for i in range(len(nums)):
            if i > ans:
                return False
            curr = i + nums[i]
            ans = max(ans, curr)
        return ans >= len(nums) - 1
# @lc code=end
