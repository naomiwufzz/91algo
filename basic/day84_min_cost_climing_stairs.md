### 思路

动规。

每个台阶都是上一级或者上两级走上来的，因此有动规方程：

dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

### 代码

~~~python
class Solution:
    def minCostClimbingStairs(self, cost):
        taijie_n = len(cost)
        dp = [0] * (taijie_n+1)
        for i in range(2, taijie_n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[taijie_n]
~~~

### 复杂度分析

- 时间复杂度：遍历一遍cost。O(N)
- 空间复杂度：O(N)

