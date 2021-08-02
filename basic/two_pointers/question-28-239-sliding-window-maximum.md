# 35.搜索插入的位置

~~~typora
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路1：暴力

按题意暴力，超出时间限制

### 代码

~~~python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        result = []
        while right <= len(nums):
            result.append(max(nums[left:right]))
            left += 1
            right += 1
        return result

~~~

### 复杂度分析

- 时间复杂度：O(n*k) 
- 空间复杂度：O(1)

## 思路2：单调队列

维护一个单调递减的双端队列，核心思路是，右指针见到的数，如果是比队列中之前见过的数小的话，有可能在窗口往后滑动的时候这个小的数成为后面的最大的数，如果见到比队列中见过的数大的话，说明前面的更小的数都没用了，这个更大的数比较有价值。

### 代码

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = list() # 单调队列
        res = list()
        for right in range(len(nums)):
            # 如果队列不是空的，且当前看的元素（right指向的元素）比队列末尾的元素大，就要逐个从后面出队，直到队列末尾比当前看的元素大或者队列空了为止
            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()
            # 队列末位保证比right大了，right入队
            queue.append(right)
            # 判断左边：
            # 左位置
            left = right - k + 1
            # 判断队列第一个数是否在窗口中，不在的话踢出
            if queue[0] < left:
                queue.pop(0)
            # 判断右边：右边只要大于k就可以逐一计算
            if right >= k-1:
                res.append(nums[queue[0]])
        return res
            
```

### 复杂度分析

- 时间复杂度：O(n) 
- 空间复杂度：O(k)