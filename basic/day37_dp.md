### 思路

#### 动态规划

比较典型的动归问题，到第n阶台阶，只可能是走上来一步或者走上来两步，所以可以得到公式` f(i) = 1*f(i-1) + 1*f(i-2)`。也就是`dp[n]=dp[n−1]+dp[n−2]`。需要初始化`dp[1]=1, dp[2]=2`

### 代码

~~~python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


~~~

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(n)

