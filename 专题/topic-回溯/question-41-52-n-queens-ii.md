# **52.N皇后**

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



## 思路：回溯

最后的结果每列每行都有一个皇后，从最左边第一列开始放置。（理解的部分在注释中，剩下的没有完全明白）

### 代码

~~~python
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 初始化列、两个对角线。用三个集合分别记录每列及两个方向对角线是否有皇后
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        def backtrack(row):
            if row == n:
                return 1
            else:
                count = 0
            for i in range(n):
                # 如果列，两条对角线上有queen，这个位置就不能放
                if i in columns or row-i in diagonal1 or row+i in diagonal2:
                    continue
                columns.add(i)
                diagonal1.add(row-i)
                diagonal2.add(row+i)
                # 继续进入下一行进行下一行的每一列判断
                count += backtrack(row+1)
                # 回溯删除
                columns.remove(i)
                diagonal1.remove(row-i)
                diagonal2.remove(row+i)
            return count
        return backtrack(0)
~~~

### 复杂度分析

- 时间复杂度：O(N!)
- 空间复杂度：O(n)

