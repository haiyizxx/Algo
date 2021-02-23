#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        candidates.sort()
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        self.dfs(target, 0, curr, ans, counter)
        return ans

    def dfs(self, target, start, curr, ans, counter):
        if target == 0:
            ans.append(curr[:])
            return
        elif target < 0:
            return

        for i in range(start, len(counter)):
            num, freq = counter[i]
            if freq <= 0:
                continue

            curr.append(num)
            counter[i] = (num, freq-1)
            self.dfs(target - num, i, curr, ans, counter)
            curr.pop()
            counter[i] = (num, freq)


# @lc code=end
