# 746.最小花费爬楼梯

~~~typora
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

 

示例 1：

输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
 示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
 

提示：

cost 的长度范围是 [2, 1000]。
cost[i] 将会是一个整型数据，范围为 [0, 999] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：动态规划

`dp[i]`表示到达下标`i`的最小花费，到达`0、1`最小花费是0，因为可以直接选为起始点。

### 代码

~~~python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ladder_length = len(cost)
        dp = [0] * (ladder_length + 1) # dp[0] 和 dp[1]都是0，不用另外初始化
        
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[ladder_length]
~~~

### 复杂度分析

- 时间复杂度：O(n) 
- 空间复杂度：O(n)

