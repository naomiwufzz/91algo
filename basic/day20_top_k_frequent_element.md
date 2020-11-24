### 思路

用hash先存储值和频率，再排序获得频率最高的topk

### 代码

~~~python
class Solution:
    def topKFrequent(self, nums, k: int):
        if len(nums) < 1:
            return None
        freq ={}
        for i in range(len(nums)):
            value = nums[i]
            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1
        top_values = []

        top = sorted(freq.values(), reverse=True)[:k]
        for key, v in freq.items():
            if v in top:
                top_values.append(key)
        return top_values
~~~

### 复杂度分析

时间复杂度：O(NlogN)

空间复杂度：O(N)

