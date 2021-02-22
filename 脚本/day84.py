class Solution:
    def minCostClimbingStairs(self, cost):
        taijie_n = len(cost)
        dp = [0] * (taijie_n+1)
        for i in range(2, taijie_n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[taijie_n]

class Solution:
    def min_cost(self, n):
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n] % 10007