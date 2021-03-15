#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement2(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def removeElement(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0

        n = len(nums)
        i = 0

        while(i < n):
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return i
# @lc code=end
