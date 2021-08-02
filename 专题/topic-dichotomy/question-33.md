# **Kth-Pair-Distance**

~~~typora
Given a list of integers nums and an integer k, return the k-th (0-indexed) smallest abs(x - y) for every pair of elements (x, y) in nums. Note that (x, y) and (y, x) are considered the same pair.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 5, 3, 2]
k = 3
Output
2
Explanation
Here are all the pair distances:

abs(1 - 5) = 4
abs(1 - 3) = 2
abs(1 - 2) = 1
abs(5 - 3) = 2
abs(5 - 2) = 3
abs(3 - 2) = 1
Sorted in ascending order we have [1, 1, 2, 2, 3, 4].
~~~

## 题目解读



## 思路：能力二分+双指针

暴力是超时的。二分的思路是，第一步：确定边界，本题的边界最小是0（两个数一样），最大是`max(A)-min(A)`；第二步，找第k个小的diff，相当于，有一个（虚拟的且升序）的diff数组，找第k小的，那就是能力二分（第一个最小版本思路），那么问题就是对于每个diff值，要找有几个比它小的diff（因为没有实际的diff数组，需要对每个进行计算）；第二步的子问题就变成对一个升序数组和一个int diff来说，有多少对数的绝对值小于diff，用双指针来解决，问题变成，遍历右指针，对于每个右指针`j`来说，左指针和右指针指向的数绝对值`<=`都可以算在里面，所以把左指针指到刚好两个指针绝对值`<=dff`就可以。

### 代码

~~~python
class Solution:
    def solve(self, A, k):
        A = sorted(A)
        def count_not_greater(diff):
            # 计算A中距离小于diff的数共有多少对
            i = 0
            ans = 0
            for j in range(1, len(A)): # j是右指针
                while A[j] - A[i] > diff:
                    i += 1 # i不需要重置，因为i左边的肯定不满足下一个j
                ans += j - i
            return ans

        l, r = 0, A[-1]-A[0] # 定义上下边界，最小0，最大是max-min
        while l <= r:
            mid = (l + r) // 2
            if count_not_greater(mid) > k: # 小于mid的数对多于k个，说明mid大了
                r = mid - 1
            else:
                l = mid + 1
        return l

~~~

### 复杂度分析

- 时间复杂度：O(nlogn) 
- 空间复杂度：看排序

