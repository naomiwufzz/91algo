# 198.打家劫舍

~~~typora
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：dp(lis问题)

动态规划。

1. 可以用两个动归状态：第一个用来记录到`nums[i]`为止的最长递增子序列长度，第二个用来记录到`nums[i]`未知的最长递增子序列个数。

2. 状态转移

   对于每个`nums[i]`，如果之前的数`nums[j]`比`nums[i]`小，那么到`nums[j]`为止的最长递增子序列长度到位置`i`增加了1

### 代码

~~~python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        lengths = [0] * n # 用于记录最长子序列长度
        counts = [1] * n # 用于记录具有最长子序列的序列数量
        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]: # 说明i到j递增
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i] # j比i的最长子序列要长1位
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

~~~

### 复杂度分析

- 时间复杂度：O(n^2) 
- 空间复杂度：O(n)

