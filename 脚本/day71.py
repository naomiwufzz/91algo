# 方法1：求和。数学的小技巧。
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        target_sum = (0 + n) * (n + 1) // 2
        result = target_sum - sum(nums)
        return result

# 方法2：位运算
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        res = n
        for i, num in enumerate(nums):
            res = res ^ i
            res = res ^ num
        return res


print(Solution().missingNumber([3,0,1]))