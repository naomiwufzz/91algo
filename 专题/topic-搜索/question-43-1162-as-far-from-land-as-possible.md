# **1162.地图分析**

~~~typora
你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。

如果网格上只有陆地或者海洋，请返回 -1。

 

示例 1：



输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
示例 2：



输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
 

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：bfs

往四个方向进行广度优先搜索，图和树的bfs不一样的是，树是有root的，图是需要把所有源点先入队；另外，图需要标记访问过的地方（直接设置成已访问）。那么这里就是，把所有陆地（1）都入队，最后扩散到的就是最远的海洋

### 代码

~~~python
import collections
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        # 存储1的位置
        queue = collections.deque([(i, j) for i in range(n) for j in range(n) if grid[i][j]==1])
        # 没有1或者全是1的情况（全是陆地或者海洋）直接返回
        if len(queue) == 0 or len(queue) == n ** 2:
            return steps
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft() # 从左上开始搜索，pop出1的坐标
                for xi, yj in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if xi >= 0 and xi < n and yj >=0 and yj <n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1 # 见过的置-1
            steps +=1
        return steps
~~~

### 复杂度分析

- 时间复杂度：O(n^2) 
- 空间复杂度：O(n^2)

