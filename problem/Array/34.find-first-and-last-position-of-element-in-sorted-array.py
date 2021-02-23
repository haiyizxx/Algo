#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.find_left(nums, target), self.find_right(nums, target)]

    def find_left(self, nums, target):
        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        print('left return')
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        return -1

    def find_right(self, nums, target):
        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        return -1

# @lc code=end
