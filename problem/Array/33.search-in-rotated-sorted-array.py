#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    # e.g.
    # 0 1 2 4 5 6 7
    # 4 5 6 7 0 1 2
    #  upper half
    #    /     |
    #   /      |
    #  /       |
    # ----------------
    #          |      /
    #          |     /
    #          |    /  lower half

    # if mid in upper half, mid > left
    # if mid in lower hal, mid < left
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # mid in upper half
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
# @lc code=end
