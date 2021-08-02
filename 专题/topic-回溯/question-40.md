# **Number of Operations to Decrement Target to Zero**

~~~typora
You are given a list of positive integers nums and an integer target. Consider an operation where we remove a number v from either the front or the back of nums and decrement target by v.

Return the minimum number of operations required to decrement target to zero. If it's not possible, return -1.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [3, 1, 1, 2, 5, 1, 1]
target = 7
Output
3
Explanation
We can remove 1, 1 and 5 from the back to decrement target to zero.

Example 2
Input
nums = [2, 4]
target = 7
Output
-1
Explanation
There's no way to decrement target = 7 to zero.
~~~

## 题目解读



## 思路：滑动窗口

这题非常常见，是一种逆向思维的滑动窗口的应用。根据题目，求解两端，可以联想到中间的部分是连续的，可以反向思考使用滑动

### 代码

~~~python
class Solution:
    def solve(self, A, target):
        if not A and not target:
            return 0
        # 把问题转换成找中间连续数组的和是否可以是target
        target = sum(A) - target
        # 初始化ans,左指针，当前和
        ans = len(A) + 1
        l = 0
        t = 0
        for r in range(len(A)):
            t += A[r]
            while l <= r and t > target: # 注意左边不能越界
                t -= A[l]
                l += 1
            if t == target:
                ans = min(ans, len(A)-(r-l+1))
        return -1 if ans == len(A)+1 else ans
~~~

### 复杂度分析

- 时间复杂度：O(N)
- 空间复杂度：O(1)

