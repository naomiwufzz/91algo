# 40.组合总和2

~~~typora
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
 

提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：回溯+剪枝

跟昨天的有点像，区别在于昨天的是可以重复取用的

### 代码

~~~python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0: # 说明找到了
                res.append(path) # 这里注意，如果append path，等path变了，结果也会变
                return
            for idx in range(begin, len(candidates)):
                if candidates[idx] > residue: # 这个idx比res大说明后面都比它大不用考虑了
                    break
                if idx > begin and candidates[idx] == candidates[idx-1]: # 说明遇到重复的数了，结果是一样的
                    continue

                # path.append(candidates[idx])
                dfs(idx+1, path+[candidates[idx]], residue-candidates[idx]) # 直接加和append再pop是不一样的
                # path.pop() # 这里体现回溯

        if len(candidates) == 0: # 特殊情况
            return []

        res = []
        candidates.sort()
        dfs(0, [], target)
        return res
~~~

### 复杂度分析

- 时间复杂度：最坏情况 O(n^(target/min)) ，n是数组长度，min是数组最小的元素值，target/min是递归栈最大深度
- 空间复杂度：O(target^2)

