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



## 思路：dp

动态规划。考虑`dp[i]`表示到第`i`间房子可以打劫到的最大金额。那么`i`屋子。要么打劫，要么不打劫，取决于什么情况金额最大。动归方程就是`dp[i]=max(dp[i−2]+nums[i],dp[i−1])`

### 代码

~~~python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        house_num = len(nums)
        if house_num == 1:
            return nums[0]
        dp = [0] * house_num
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, house_num):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
~~~

### 复杂度分析

- 时间复杂度：O(n) 
- 空间复杂度：O(n)

