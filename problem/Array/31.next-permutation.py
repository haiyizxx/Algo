#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    # i is left index
    def reverse(self, nums, i):
        left = i
        right = len(nums) - 1
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: find first desending number, x
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i == -1:
            self.reverse(nums, 0)
            return

        # Step 2: find the first num y, that y > x
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap x, y
        self.swap(nums, i, j)

        # Step 4: Reverse nums after x
        self.reverse(nums, i+1)

# @lc code=end
