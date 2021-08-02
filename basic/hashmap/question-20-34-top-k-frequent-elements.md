# 347.前k个高频元素

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

先用哈希表记录频率。再两次循环哈希表获得topk大的频率对应的值。但要注意，自己一开始写的排序，用了python内置的`min()`函数，复杂度是`O(n)`。需要优化

### 代码

~~~python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = dict()
        # 获取频率哈希表
        for n in nums:
            if n not in hash_table:
                hash_table[n] = 1
            else:
                hash_table[n] += 1
        topk_freq_lis = []
        for n, freq in hash_table.items():
            if len(topk_freq_lis) < k:
                topk_freq_lis.append(freq)
            else:
                topk_freq_lis.append(freq)
                topk_freq_lis.remove(min(topk_freq_lis))
        result = []
        for n, freq in hash_table.items():
            if freq in topk_freq_lis:
                result.append(n)
        return result
~~~

### 复杂度分析

- 时间复杂度：O(n) 遍历
- 空间复杂度：O(n*n) 




