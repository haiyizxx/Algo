#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]

        r_s, r_e = 0, n-1
        c_s, c_e = 0, n-1

        counter = 1
        while r_s <= r_e and c_s <= c_e:
            # from left to right
            for i in range(c_s, c_e+1):
                res[r_s][i] = counter
                counter += 1
            r_s += 1

            # from top to down
            for i in range(r_s, r_e+1):
                res[i][c_e] = counter
                counter += 1
            c_e -= 1

            # from right to left
            for i in range(c_e, c_s-1, -1):
                res[r_e][i] = counter
                counter += 1
            r_e -= 1

            # from down to top
            for i in range(r_e, r_s-1, -1):
                res[i][c_s] = counter
                counter += 1
            c_s += 1

        return res
# @lc code=end
