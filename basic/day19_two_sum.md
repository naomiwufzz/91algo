### 思路

用哈希map 即python中的字典

key是target-num

value是idx

### 代码

~~~python
class Solution:
    def twoSum(self, nums, target: int):
        dic = dict()
        for i, num in enumerate(nums):
            if num not in dic:
                dic[target-num] = i
            elif num in dic:
                return [dic[nums[i]], i]
~~~

### 复杂度分析

时间复杂度：O(N)

空间复杂度：O(N)

