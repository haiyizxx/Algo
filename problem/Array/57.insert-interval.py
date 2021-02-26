#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            i += 1
        intervals.insert(i, newInterval)

        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        # l interval < newInterval
        # r interval > newInterval
        l, r = [], []

        for interval in intervals:
            if interval[1] < s:
                l.append(interval)
            elif interval[0] > e:
                r.append(interval)
            else:
                s = min(s, interval[0])
                e = max(e, interval[1])
        return l + [[s, e]] + r

        return ans

# @lc code=end
