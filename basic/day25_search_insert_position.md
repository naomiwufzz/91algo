### 思路

二分查找方法。

要注意的是，退出的情况需要是left==right，不然计算到底最后输出left还是right会很复杂

### 代码

~~~python
class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        left = 0
        right = length-1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
        return left

~~~

### 复杂度分析

- 时间复杂度：O(logN)
- 空间复杂度：O(1)

