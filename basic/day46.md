### 思路

用并查集是比较方便的。如果连接数小于 n - 1，那就直接返回 -1。如果n-1小于等于connection的长度，那么我们统计出图中的连通分量数 `k`，返回 `k - 1`

### 代码

~~~python
class Solution:
    def makeConnected(self, n, connections) -> int:
        if len(connections) < n - 1: # 如果连接数小于 n - 1，那就直接返回 -1
            return -1

        fa = [x for x in range(n)]

        def findset(x):
            if x != fa[x]:
                fa[x] = findset(fa[x])
            return fa[x]

        part = n
        for c0, c1 in connections:
            p, q = findset(c0), findset(c1)
            if p != q:
                part -= 1
                fa[p] = q

        return part - 1
~~~

### 复杂度分析

- 时间复杂度：O*(*N*log*N*+*M)
- 空间复杂度：*O*(*N*)

