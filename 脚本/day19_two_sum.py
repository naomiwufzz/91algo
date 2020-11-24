class Solution:
    def twoSum(self, nums, target: int):
        dic = dict()
        for i, num in enumerate(nums):
            if num not in dic:
                dic[target-num] = i
            elif num in dic:
                return [dic[nums[i]], i]

nums = [2, 7, 11, 15]
target = 9
sol = Solution().twoSum(nums, target)
print(sol)
