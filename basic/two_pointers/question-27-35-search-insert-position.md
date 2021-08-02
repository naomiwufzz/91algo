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



## 思路：二分

二分法，要注意循环要能够退出

### 代码

~~~python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left = 0 
        right = len(nums)-1
        while left <= right:
            target_pos = (left+right) // 2
            if nums[target_pos] > target:
                right = target_pos-1  # 既然不等于了，target位置没意义了，可以减一
            elif nums[target_pos] < target:
                left = target_pos+1
            else:
                return target_pos
        return left
~~~

### 复杂度分析

- 时间复杂度：O(logn) 二分
- 空间复杂度：O(1)


