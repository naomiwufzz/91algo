#### [560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)

### 思路

一开始用暴力法，枚举所有的i和j。这样会超出时间限制

用前缀和的方法，存储目前见过的所有前缀和，放在字典中。假设从`i`位置到`j`位置的子串和是`k`，这里`i!=j`，如果相等中间就是空的了。那么`0`位置到`i`位置的和和`0`位置到`j`位置的和的差一定就等于`k`

### 代码

~~~python
# 暴力法
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

# 前缀和
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

            # 更新字典必须在求和之后（这里卡了很久）。不然会得到匹配上但是对应的字串是空集的情况
            # 其实就是，i和j不能相等。不然子串是空
            if pre_sum in count_of_sum:
                count_of_sum[pre_sum] += 1
            else:
                count_of_sum[pre_sum] = 1
        return result

~~~

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(n)

