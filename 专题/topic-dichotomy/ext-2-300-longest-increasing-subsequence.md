# 300.最长递增子序列

~~~typora
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路1：动归

对于数组每个位置`i`，其最长递增子序列，一定是`0`到`i-1`位置中能够和`i`位置数组成递增的串加一

### 代码

~~~python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return None
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i): # 遍历一遍i位置前面的数
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
~~~

### 复杂度分析

- 时间复杂度：O(n^2) 
- 空间复杂度：O(n)

