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

