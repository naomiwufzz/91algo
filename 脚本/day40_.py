class Solution:
    def subarraySum(self, nums, k):
        # 暴力法会超出时间
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                if nums[i:j] and sum(nums[i:j]) == k:
                    result += 1
                if j + 1 < len(nums)-1 and nums[j+1] != 0:
                    continue
        return result

class Solution:
    def subarraySum(self, nums, k):
        pre_sum = 0
        count_of_sum = {0:1}
        result = 0
        for i in range(len(nums)):
            pre_sum += nums[i]

            needed_diff = pre_sum - k
            if needed_diff in count_of_sum:
                result += count_of_sum[needed_diff]

            # 更新字典必须在求和之后。
            if pre_sum in count_of_sum:
                count_of_sum[pre_sum] += 1
            else:
                count_of_sum[pre_sum] = 1
        return result








num = [1, -1, 2, -2]
k = 1
print(Solution().subarraySum(num, k))