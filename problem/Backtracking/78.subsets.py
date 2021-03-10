#
# @lc app=leetcode id=78 lang=python3
#
#
# [78] Subsets

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        self.backtrack(nums, 0, res, [])
        return res

    def backtrack(self, nums, idx, res, tmp):
        res.append(tmp[:])

        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            self.backtrack(nums, i+1, res, tmp)
            tmp.pop()

            # @lc code=end
