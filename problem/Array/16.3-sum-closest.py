#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n):
            if i and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(target - temp) < abs(target - ans):
                    print([nums[i], nums[j], nums[k]])
                    ans = temp
                if temp > target:
                    k -= 1
                elif temp < target:
                    j += 1
                else:
                    return temp
                # while (j < k and nums[j] == nums[j+1]):
                #     j += 1
                # while (j < k and nums[k] == nums[k-1]):
                #     k -= 1
                # j += 1
                # k -= 1
        return ans

# @lc code=end
