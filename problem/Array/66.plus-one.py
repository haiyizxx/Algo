#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        while (pos >= 0):
            if digits[pos] < 9:
                digits[pos] += 1
                return digits

            # key
            digits[pos] = 0
            pos -= 1

        digits.insert(0, 1)
        return digits

# @lc code=end
