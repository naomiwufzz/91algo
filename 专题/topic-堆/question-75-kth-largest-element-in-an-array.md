# 215.数组中第k大的元素

~~~typora
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

 

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
 

提示：

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：小顶堆

固定一个`k`大小的堆，这样堆顶以下有`k-1`个比堆顶大的数，最后取堆顶即可（还需要练习堆实现的代码）

### 代码

~~~python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # 维护一个长度为k的小顶堆，那么这个堆有k个数比它大，最后取堆顶即可
        # 先初始化一个大小为k的小顶堆，依次入堆
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            # 弹出最小的元素被新的元素替代
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]


~~~

### 复杂度分析

- 时间复杂度：O(nlogk) 
- 空间复杂度：O(k) 堆大小是k

