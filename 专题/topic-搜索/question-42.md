# **52.岛屿的最大面积**

~~~typora
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

 

示例 1：


输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：1
 

提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：dfs

需要找到所有岛屿的面积，取其中最大值；其中，找到所有岛屿的面积的思路是：

（1）从某个位置出发（也就是发现是1），向四个方向找土地（也就是1）

（2）没找到一个土地（也就是1）计数要加一

（3）确保每块土地只会被探寻一次

利用**图的遍历**（dfs或者bfs）。dfs思路：遍历二位数组，找到陆地，对陆地上下左右进行递归方式的dfs。递归的时候要找递归边界递归边界有两个，一个是图的大小一个是遍历到水。

### 代码

~~~python
class Solution:
    def dfs(self, grid, cur_i, cur_j):
            # 递归出口两个条件，cur_i 和cur_j 在grid中；且gird[i][j]是1
            if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                return 0
            grid[cur_i][cur_j] = 0 # 当前点直接设为0就不会重复搜索
            ans = 1
            # 上下左右dfs
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ans += self.dfs(grid, cur_i+di, cur_j+dj)
            return ans
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

~~~

### 复杂度分析

- 时间复杂度：O(m*n) m是行n是列。最大的情况下，递归深度是整个网格大小（全是1），那就是行\*列
- 空间复杂度：O(m*n)

