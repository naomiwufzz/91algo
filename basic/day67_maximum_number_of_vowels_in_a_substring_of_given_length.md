### 思路

用双指针+滑动窗口的思路（似乎不用哈希?）。因为k的长度是固定的，所以比较好定窗口，先把右指针移到k的地方，记录初始窗口元音数量。然后左右指针一起向右移动，如果右边看到元音（滑进来）总数就增加，同时如果左边滑出去的是原因总数就减少

### 代码

~~~python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        alpha = {'a', 'e', 'i', 'o', 'u'}
        left, right = 0, 0
        num_alpha = 0
        while right < k:  # 先把窗口右边移到k的地方，并记录元音数量
            if s[right] in alpha:
                num_alpha += 1
            right += 1
        max_alpha = num_alpha
        while k <= right < len(s):
            if s[right] in alpha:
                num_alpha += 1
            if s[left] in alpha:
                num_alpha -= 1
            max_alpha = max(num_alpha, max_alpha)
            right += 1
            left += 1

        return max_alpha
~~~

### 复杂度分析

- 时间复杂度：O(N)
- 空间复杂度：O(1)

