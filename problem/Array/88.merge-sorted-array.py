#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = len(nums1)-len(nums2)-1, len(nums2)-1
        ptr = len(nums1)-1
        while ptr >= 0:
            if ptr2 < 0:
                break
            if ptr1 >= 0 and nums1[ptr1] >= nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1

# @lc code=end
