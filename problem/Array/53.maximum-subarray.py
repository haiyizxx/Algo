#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    # nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # f:    [-2, 1, -2, 4, 3, 5, 6, 1, 5]
    # f[i] = maxSubarray(0...i)
    # f[i] = f[i-1] > 0? nums[i] + f[i-1] : nums[i]
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            if f[i-1] > 0:
                f[i] = f[i-1] + nums[i]
            else:
                f[i] = nums[i]
        return max(f)

    def maxSubArray3(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        s = nums[0]
        for i in range(1, n):
            if s > 0:
                s += nums[i]
            else:
                s = nums[i]

            ans = max(ans, s)
        return ans

    def maxSubArray(self, nums: List[int]) -> int:

        def cross_sum(nums, l, r):
            if l == r:
                return nums[l]
            mid = l + (r - l) // 2
            left_sub_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, l - 1, -1):
                curr_sum += nums[i]
                left_sub_sum = max(left_sub_sum, curr_sum)

            right_sub_sum = float('-inf')
            curr_sum = 0
            for i in range(mid+1, r+1):
                curr_sum += nums[i]
                right_sub_sum = max(right_sub_sum, curr_sum)
            return left_sub_sum + right_sub_sum

        def recur(nums, l, r):

            if l >= r:
                return nums[l]

            mid = l + (r - l) // 2

            l_sum = recur(nums, l, mid)
            r_sum = recur(nums, mid+1, r)
            cs = cross_sum(nums, l, r)

            return max(l_sum, r_sum, cs)

        return recur(nums, 0, len(nums)-1)

# @lc code=end
