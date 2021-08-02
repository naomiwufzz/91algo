# 39.组合总和

~~~typora
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

 

示例 1：

输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
示例 4：

输入: candidates = [1], target = 1
输出: [[1]]
示例 5：

输入: candidates = [1], target = 2
输出: [[1,1]]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：回溯+剪枝

这里的剪枝体现在，展开深度优先搜索的时候，如果是已经用过的数值，不需要再作为后续的候选数值了，因为已经用过的数值的可能组合已经全部搜索过了

### 代码

~~~python
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            """
            candidates:候选数组
            begin：搜索起点
            target：目标值。每减去一个值，target会变小  
            path：从根节点到叶子节点的路径，是一个栈
            res：结果集列表          
            """
            if target < 0: # target是负值就不再产生新的子节点
                return
            if target == 0: 
                res.append(path)
            for idx in range(begin, size):
                dfs(candidates, idx, size, path+[candidates[idx]], res, target-candidates[idx]) # 用过的idx不用用了，begin往后移，因为对于每个用过的分支，已经搜索过全部的解空间了。这里的回溯体现在，path+[candidates[idx]]python里面path直接是list扩展了

        size = len(candidates)
        if size == 0:
            return []
        path, res = [], []
        dfs(candidates, 0, size, path, res, target)
        return res
~~~

### 复杂度分析

- 时间复杂度：最坏情况 O(n^(target/min)) ，n是数组长度，min是数组最小的元素值，target/min是递归栈最大深度
- 空间复杂度：O(target^2)

