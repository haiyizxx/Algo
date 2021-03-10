#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right_boundary_0, left_boundary_2 = 0, len(nums)-1
        curr = 0
        while curr <= left_boundary_2:
            if nums[curr] == 0:
                nums[right_boundary_0], nums[curr] = nums[curr], nums[right_boundary_0]
                right_boundary_0 += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[left_boundary_2], nums[curr] = nums[curr], nums[left_boundary_2]
                left_boundary_2 -= 1
                # no increment here becuase nums[left_boundary] might be 0

# @lc code=end
