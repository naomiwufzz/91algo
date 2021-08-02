# 435.无重叠区间

~~~typora
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：贪心

按照右边界排序，只加下一个最近的不重叠的区间。右边界越小，留给下一个区间的空间就越多，所以从左向右遍历，这样就自然能够选到右边界小的。

因为题目只要求返回一个数量，不用删除原来的`intervals`

### 代码

~~~python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1]) # 按右边界升序
        count = 1 # 不相交边界至少有一个
        end = intervals[0][1] # 初始化第一个end
        for st, ed in intervals:
            if st >= end: # 上一个边界是end
                count += 1
                end = ed
        return len(intervals)-count

~~~

### 复杂度分析

- 时间复杂度：(nlogn)  需要排序
- 空间复杂度：O(logn) 排序需要使用栈空间

