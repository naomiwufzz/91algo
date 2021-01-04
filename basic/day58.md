### 思路

可以直接用排序的方法查找，把matrix变成list，比较粗暴；

堆的思路，也就是归并排序，在整个矩阵中，每次弹出矩阵中最小的值，第k个被弹出的就是我们需要的数字。

### 代码

~~~python
# 排序
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        list_of_matrix = sorted(sum(matrix, []))
        return list_of_matrix[k - 1]

# 堆
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        if not matrix or not matrix[0] or k <= 0: return

        rows, cols = len(matrix), len(matrix[0])
        # 初始化第一列为堆的初始状态，元组为 (val, i, j)
        h = [(matrix[i][0], i, 0) for i in range(rows)]
        heapq.heapify(h)

        res = 0
        for i in range(k):
            res, i, j = heapq.heappop(h)
            if j != cols - 1:   # 不是当前行最后一个元素的话，则追加本行下一个元素。
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
        return res

~~~

### 复杂度分析

- 时间复杂度：O(n^2log(k))
- 空间复杂度：O(k)

