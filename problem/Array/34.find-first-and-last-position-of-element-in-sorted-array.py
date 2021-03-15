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

    # Left range binary search
    def find_left(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                #[left, mid-1]
                right = mid-1
            else:
                #[mid+1, right]
                left = mid+1

        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    # Right range binary search
    def find_right(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                #[mid+1, right]
                # Move from left to right, shrink the range towards right
                left = mid + 1
            else:
                #[left, mid-1]
                right = mid - 1

        if right < 0 or nums[right] != target:
            return -1
        return right

# @lc code=end
