#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, curr, ans)
        return ans

    def dfs(self, candidates, target, start, curr, ans):
        if target == 0:
            ans.append(curr[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            curr.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, curr, ans)
            curr.pop()


# @lc code=end
