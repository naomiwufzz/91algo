# 78.子集

~~~typora
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

这题很经典，需要掌握位运算；combination和permutation的回溯dfs

## 思路1：位运算

nums种的数字要不选要不不选，用0-1表示。遍历每一种0-1组合，对每种组合判断哪些数选了哪些数没选

### 代码

~~~python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 对于nums来说，每个元素，选或者不选有两个选择，总的集合数量一定是2^len(nums)
        # 要组合2^n种0-1
        res = []
        comb = 1 << len(nums) # 比如三个数字，1左移3位是1000
        for i in range(comb): # i 是一种0-1组合.range到comb是不包含comb的
            subset = []
            for j in range(len(nums)):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
~~~

### 复杂度分析

- 时间复杂度：O(n2^n)  每种选择都过了一遍
- 空间复杂度：O(n)subset用来存储中间的子集

