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



## 思路：贪心+双指针

先排序。让重的人先看看能不能和最轻的人组合，可以的话送走，不可以就最重的自己走。

### 代码

~~~python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) <= 1:
            return len(people)
        people = sorted(people)
        start = 0
        end = len(people)-1
        res = 0
        while start <= end:
            if people[end] + people[start] <= limit:
                res + 1
                start += 1
                end -= 1
            else:
                res += 1
                end -= 1

        return res
~~~

### 复杂度分析

- 时间复杂度：O(nlogn)  需要排序
- 空间复杂度：O(1) 

