# 1054.距离相等的条形码

~~~typora
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

 

示例 1：

输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：

输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
 

提示：

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distant-barcodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：堆+贪心

先按频率堆化，形成大顶堆，按高频率一对一对取出穿插排列，最后如果剩一个就拼到最后，如果不剩就排完了

### 代码

~~~python
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = dict()
        # 获得元素频次，并根据频次heapify
        for barcode in barcodes:
            cnt[barcode] = cnt.get(barcode, 0) + 1
        heap = [(-freq, val) for val, freq in cnt.items()]
        heapq.heapify(heap) # maxheap
        res = []
        # 根据最高的频次两个两个隔位放进res
        while len(heap) >= 2:
            fx, x = heapq.heappop(heap)
            fy, y = heapq.heappop(heap)
            res += [x, y]
            if (-fx) - 1 > 0:
                heapq.heappush(heap, (fx + 1, x))
            if (-fy) - 1 > 0:
                heapq.heappush(heap, (fy + 1, y))
        if heap:
            res.append(heap[0][1])
        return res

~~~

### 复杂度分析

- 时间复杂度：O(n+klog(k))
- 空间复杂度：O(k) 

