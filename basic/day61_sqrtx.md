### 思路

用二分法找。要注意取整。

### 代码

~~~python
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                result = mid  # 因为是向下取，所以在这里要存储result
                left = mid + 1
            else:
                right = mid - 1
        return result
~~~

### 复杂度分析

- 时间复杂度：O(logn)
- 空间复杂度：O(1)

