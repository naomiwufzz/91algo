# 322.零钱兑换

~~~typora
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：dp背包问题

转换成完全背包问题。`dp[i]`表示填满容量为`i`的背包需要的最小的硬币数量，把`amount`当作是背包的容量，那么我们需要找的就是`dp[amount]`，对每个`dp[i]`来说，最少需要的硬币是之前填满`i`需要的硬币和填满`i-coin`的容量需要的硬币加`1`（因为coin自己算1个）

### 代码

~~~python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount  # dp[0]是0，后面的最大为10001 dp[i]表示填满容量为i的背包需要的最少硬币数量 
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1) # i一定大于coin
        return -1 if dp[-1]==10001 else dp[-1]
~~~

### 复杂度分析

- 时间复杂度：(n*amount) 
- 空间复杂度：O(amount)

