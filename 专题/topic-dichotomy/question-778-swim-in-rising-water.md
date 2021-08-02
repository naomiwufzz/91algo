# **778.水位上升的泳池中游泳**

~~~typora
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

 

示例 1:

输入: [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例2:

输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
 

提示:

2 <= N <= 50.
grid[i][j] 是 [0, ..., N*N - 1] 的排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swim-in-rising-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：计数二分+小岛问题dfs

对于最小的`t`值，更小的都不行，更大的都行，所以可以想到最左二分，直接套最左二分，边界最小是0，最大是grid中最大的数；剩下的问题就是，判断对某`t`值，是否有路径能够到右下角，这个可以用dfs中的小岛子问题解决（没有完全理解，还需要练习下小岛问题）

### 代码

~~~python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen = set()
        def test(mid, x, y):
            # dfs中的小岛子问题。判断mid是否比坐标x,y大（不小于）
            # x或者y越界，不考虑
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0]) - 1:
                return False
            # mid如果小于坐标x, y说明mid不成立
            if grid[x][y] > mid:
                return False 
            # mid不小于x, y且x, y坐标已经到达目标坐标，就是True
            if (x, y) == (len(grid)-1, len(grid[0]) - 1):
                return True
            if (x, y) in seen:
                return False
            seen.add((x, y))
            return test(mid, x+1, y) or test(mid, x-1, y) or test(mid, x, y+1) or test(mid, x, y-1)
            
        left = 0
        right = max([max(vec) for vec in grid]) # 整个网格中最大的数就是搜索空间中最大的
        while left <= right:
            mid = (left + right) // 2
            if test(mid, 0, 0): # 说明mid成立，缩小搜索空间继续找最小的成立的数
                right = mid - 1
            else:
                left = mid + 1
            seen = set() # 更新seen
        return left
~~~

### 复杂度分析

- 时间复杂度：O(NlogM)  M是grid中最大的值，N是grid的大小
- 空间复杂度：O(N) N是grid的大小，因为有seen存储见过的数据

