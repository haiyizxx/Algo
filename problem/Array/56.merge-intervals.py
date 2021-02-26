#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])

        res = []
        cur_s, cur_e = intervals[0][0], intervals[0][1]

        for s, e in intervals[1:]:
            if s > cur_e:
                res.append([cur_s, cur_e])
                cur_s = s
                cur_e = e
            else:
                if e > cur_e:
                    cur_e = e
        res.append([cur_s, cur_e])
        return res

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        for interval in sorted(intervals, key=lambda x: x[0]):
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans
# @lc code=end
