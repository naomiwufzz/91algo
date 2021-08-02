# Shortest Cycle Containing Target Node

~~~typora
ou are given a two-dimensional list of integers graph representing a directed graph as an adjacency list. You are also given an integer target.

Return the length of a shortest cycle that contains target. If a solution does not exist, return -1.

Constraints

n, m ≤ 250 where n and m are the number of rows and columns in graph
~~~

## 题目解读



## 思路：层次遍历+哈希

层次遍历，从上往下的话，用哈希表存储横坐标，层次遍历到相同的横坐标就不管（只需要遍历到的第一个）

### 代码

~~~python
import collections
class Solution:
    def solve(self, root):
        q = collections.deque([root, 0])
        d = {}  # 哈希表用于存横坐标和值
        # 层次遍历
        while q:
            cur_root, pos = q.popleft()
            if pos not in d:  # 只看最上面的，重复的没有必要
                d[pos] = cur_root.val
            if cur_root.left:
                q.append((cur_root.left, pos-1))
            if cur_root.right:
                q.append((cur_root.right, pos+1))
        return list(map(lambda x: x[1], sorted(d.items(), key=lambda x: x[0])))  # 对哈希表排序

~~~

### 复杂度分析

- 时间复杂度：O(nlogn) 因为有排序 n是节点数
- 空间复杂度：O(n)

