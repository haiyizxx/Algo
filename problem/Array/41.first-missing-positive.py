#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start

# [3,4,-1,1]
#  0,1,2,3
# Should be [-1,1,3,4]
# when i = 0, nums[0] = 3
# 3 should be in nums[3-1] => nums[2]=-1
# nums[nums[i]-1] (-1) != nums[i](3)
#         2                    3
# switch, [-1,4,3,1], 3 back to correct position

# need use while
# [3,1,4,-1] => [4,1,3,-1] => [-1,1,3,4]
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

# @lc code=end
