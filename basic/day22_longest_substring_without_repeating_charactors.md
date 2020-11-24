### 思路

滑动窗口向前移动，用hash存储元素，当碰到重复的元素的时候，把这个元素第一次出现的索引找到，并把窗口移动到这个重复元素第一次出现的地方，hash里面把前面的都删掉。每次出现重复的时候，计算元素长度，如果比max长就记住

注意：子串长度都是相等的

### 代码

~~~python
class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        dic = {}
        i = 0
        max_length = 0
        while i < len(s):
            if s[i] not in dic:  # 当元素不在哈希表中的时候，放入哈希表，并记住位置
                dic[s[i]] = i
                i += 1
            else:
                if len(dic) > max_length:
                    max_length = len(dic)
                idx = dic[s[i]] # 找到该重复元素的位置，并删掉重复位子之前的所有元素，重新计算长度
                del_val = []

                for index, v in dic.items():
                    if v <= idx:
                        del_val.append(index)
                for val in del_val: del dic[val]
                dic[s[i]] = i
                i += 1
        if len(dic) > max_length:
            max_length = len(dic)
        return max_length
~~~

### 复杂度分析

- 时间复杂度：O(N^2)
- 空间复杂度：O(N）

