# 1319.联通网络的操作次数

~~~typora
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

 

示例 1：



输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
示例 2：



输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2
示例 3：

输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
输出：-1
解释：线缆数量不足。
示例 4：

输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
输出：0
 

提示：

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
没有重复的连接。
两台计算机不会通过多条线缆连接。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：并查集

n个网络，需要n-1条线去连接。这里可以先判断联通的线是否足够，在足够的情况下，找联通分量的个数，比1多出来几个，就需要多少条线去连接多出来的联通分量。（只要线是够的，不管怎么样都能连上，不用考虑如何连）

### 代码

~~~python
class UnionFindSet:
    def __init__(self, n):
        self.father = {}
        self.cnt = n # 联通分量的数量

    def find(self, x):
        self.father.setdefault(x, x)
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        self.father[fx] = fy
        self.cnt -= 1 # 每一次union，联通分量减掉一个

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 冗余的线要大于没有联通的cluster即可。
        # n个节点，需要n-1条边连在一起
        if len(connections) < n - 1: # 最少需要n-1个连接去联通n台机器
            return -1
        uf = UnionFindSet(n)
        for connection in connections:
            uf.union(connection[0], connection[1])
        return uf.cnt - 1 # 联通分量的数量减1
~~~

### 复杂度分析

- 时间复杂度：O(n+m)，m是connections的长度（就是图的V+E）
- 空间复杂度：O(n)  

