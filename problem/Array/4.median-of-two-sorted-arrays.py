#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        # k'th element. left median of combined array
        k = (n1 + n2 + 1) // 2

        l = 0
        r = n1
        # Binary search on nums1, compare nums1[m1] and nums2[m2-1]
        while l < r:
            # num of elements used in nums1
            m1 = l + (r - l) // 2

            # num of elemetns used in nums2
            m2 = k - m1

            if nums1[m1] < nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1

        m1 = l
        m2 = k - l

        a1 = float('-inf') if m1 <= 0 else nums1[m1-1]
        b1 = float('-inf') if m2 <= 0 else nums2[m2 - 1]
        c1 = max(a1, b1)

        if (n1 + n2) % 2 == 1:
            return c1

        a2 = float('inf') if m1 >= n1 else nums1[m1]
        b2 = float('inf') if m2 >= n2 else nums2[m2]
        c2 = min(a2, b2)

        return (c1 + c2) * 0.5

# @lc code=end
