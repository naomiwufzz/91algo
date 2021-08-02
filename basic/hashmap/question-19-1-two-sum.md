# 1.两数之和

~~~typora
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路1：哈希表

题目有些限制条件让题目变得较为简单。遍历一遍，记录之前的值和位置，只要在后续遍历的时候找到对应的`target-val`就可以

~~~python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_dic = dict() # key是值，val是位置
        for i,v in enumerate(nums):
            if target - v in hash_dic:
                return [hash_dic[target-v], i]
            if v not in hash_dic:
                hash_dic[v] = i
        return []

~~~

### 复杂度分析

- 时间复杂度：O(n) 遍历一遍
- 空间复杂度：O(n) 用一个哈希表记录值，最坏的情况遍历完，是O(n) 

## 思路2：排序+双指针

先升序，一个指针在升序表头，一个在尾，根据两个指针的数的和判断指针移动方向。注意可能会有两个值一样的情况，要重新处理idx，这个方法很麻烦，复杂度也比哈希方法高，但是是一个不错的思路

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        temp = nums.copy()
        temp = sorted(temp)
        # 两个指针各在最开始和最结尾
        left_pointer = 0
        right_pointer = len(temp)-1
        sum_vals = []
        while left_pointer != right_pointer:
            cur_sum = temp[left_pointer] + temp[right_pointer]
            if cur_sum > target:
                right_pointer -= 1
            elif cur_sum < target:
                left_pointer += 1
            elif cur_sum == target:
                sum_vals = [temp[left_pointer], temp[right_pointer]]
                break
        if not sum_vals:
            return []
        # 可能两个数同一个idx的情况
        if sum_vals[0] != sum_vals[1]:
            return [nums.index(val) for val in sum_vals]
        else:
            return [i for i in range(len(nums)) if nums[i] == sum_vals[0]]
```

### 复杂度分析

- 时间复杂度：O(nlogn) 排序的复杂度是nlogn
- 空间复杂度：O(n) 需要一个temp数组


