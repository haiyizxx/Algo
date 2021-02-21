#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        c = Counter(nums)
        res = []
        for i in range(n):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if (j-1 != i and nums[j] == nums[j-1]):
                    continue

                t = 0 - nums[i] - nums[j]

                if t < nums[j]:
                    continue

                if t not in c:
                    continue

                if c[t] >= (1 + (nums[i] == t) + (nums[j] == t)):
                    res.append([nums[i], nums[j], t])
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if (i and nums[i-1] == nums[i]):
                pass

            j = i + 1
            k = n - 1

            while(j < k):
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < - nums[i]:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    while (j < k and nums[j] == nums[j + 1]):
                        j += 1

                    while (j < k and nums[k] == nums[k - 1]):
                        k -= 1
                    j += 1
                    k -= 1
        return res


# @lc code=end
