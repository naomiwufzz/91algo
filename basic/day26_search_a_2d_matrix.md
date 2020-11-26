### 题目描述

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

```
示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
输出：false
示例 3：

输入：matrix = [], target = 0
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



### 思路

拉成一个一维向量，直接用二分查找

### 代码

~~~python

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)  # 行数
        if m < 1:
            return False
        n = len(matrix[0])  # 列数 总长度应该是 m * n
        left = 0
        right = m * n - 1

        while left <= right:  # 注意这里不可以是!=,会导致无法退出
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            elif mid_value > target:
                right = mid - 1
        return False
~~~

### 复杂度分析

- 时间复杂度：O(logN*M)
- 空间复杂度：O(1)

