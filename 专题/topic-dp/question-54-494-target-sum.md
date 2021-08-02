# 494.目标和

~~~typora
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
 

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：dp背包问题

这个和昨天一样，转化成0-1背包问题。元素就是背包的物体，元素大小是物体数量，都是1，背包大小是` sum(nums) + target`

### 代码

~~~python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # positive = (target + total / 2)
        t = sum(nums) + target
        if t % 2: # 判断能否整除
            return 0
        t = t // 2

        dp = [0] * (t+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(t, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[-1]
~~~

### 复杂度分析

- 时间复杂度：(negative∗(total+target)/2) 
- 空间复杂度：O((total+target)/2)

