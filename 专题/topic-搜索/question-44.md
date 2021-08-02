# Shortest Cycle Containing Target Node

~~~typora
ou are given a two-dimensional list of integers graph representing a directed graph as an adjacency list. You are also given an integer target.

Return the length of a shortest cycle that contains target. If a solution does not exist, return -1.

Constraints

n, m ≤ 250 where n and m are the number of rows and columns in graph
~~~

## 题目解读



## 思路：bfs

找到包含target最小的环，可以看成从target出发，广搜的方法找visited，遇到一个环的时候一定是最最短的

### 代码

~~~python
import collections
class Solution():
    def sol(self, graph, target):
        # 直接从target开始搜索
        q = collections.deque([target])
        visited = set()
        steps = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for neighber in graph:
                    if neighber not in visited:
                        q.append(neighber)
                    elif neighber == target:  # 说明已经闭环
                        return steps+1
            steps += 1
        return -1

~~~

### 复杂度分析

- 时间复杂度：O(v+e) v是节点，e是边 
- 空间复杂度：O(v)

