#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        tmp = []
        self.backtrack(nums, res, 0, tmp)
        return res

    def backtrack(self, nums, res, idx, tmp):
        res.append(tmp[:])
        print(tmp)
        for i in range(idx, len(nums)):
            print(i, idx, )
            if i != idx and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            self.backtrack(nums, res, i+1, tmp)
            tmp.pop()
# @lc code=end
