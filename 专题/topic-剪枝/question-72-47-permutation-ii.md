# 47.全排列2

~~~typora
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：回溯+剪枝

回溯要注意三个要素：1.有效结果（什么情况有效且输出）2.回溯范围和答案更新，范围是遍历nums，答案更新是在更新check之后 3.剪枝，这里有两个条件，第一个是该元素已经被使用；第二个是该元素和前一个元素相同且前一个元素还没有被使用（那么就是在前一个元素使用之后这个元素再用，反之也可以，可以画递归树看到前者更早剪枝）

### 代码

~~~python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, check):
            if len(path) == len(nums): # 说明找到了
                res.append(path)
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i>= 1 and nums[i] == nums[i-1] and check[i-1] == 0: # 0可以提前剪
                    continue
                check[i] = 1
                dfs(path+[nums[i]], check)
                check[i] = 0


        nums.sort() # 可能有重复元素排列可以看到是否需要剪枝
        res = []
        check = [0 for i in range(len(nums))] # 用于判断元素是否被使用过了
        dfs([], check)
        return res
~~~

### 复杂度分析

- 时间复杂度：最坏情况 O(n*n!) n是数组长度
- 空间复杂度：O(n)

