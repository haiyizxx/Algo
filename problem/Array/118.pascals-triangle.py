#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        lst = []
        i = 0
        while i < numRows:
            lst.insert(0, 1)
            for j in range(1, len(lst)-1):
                lst[j] = lst[j] + lst[j+1]
            res.append(lst[:])
            i += 1
        return res


# @lc code=end
