### 思路

两种思路：

- 思路1

先记录C的位置，保存成一个列表，然后计算S中每一个字符串到C的位置（直接相减取绝对值就是距离），直接取最小值。这种方法，由于要遍历C的位置，所以复杂度为 N^2

- 思路2

就是把左右距离一起算改成左边算和右边算相加，这样可以减少复杂度。即左边扫描一遍，右边扫描一遍，用一个变量记录最近的C的位置。

### 代码

```python
class Solution:
    def shortestToChar(self, S, C):
        # 复杂度O(N^2)
        distance = []
        target_index = []
        for i in range(len(S)):
            if S[i] == C:
                target_index.append(i)
        for i in range(len(S)):
            distance.append(min([abs(x - i) for x in target_index]))
        return distance

    def shortestToChar2(self, S, C):
        # 复杂度O(N)
        distance = []
        left_C = float('-inf')
        right_C = float('inf')

        # 先从左往右
        for i in range(len(S)):
            if S[i] == C:
                left_C = i
            distance.append(i - left_C)
        # 再从右往左
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                right_C = i
            distance[i] = min(distance[i], right_C-i)
        return distance
```

### 复杂度分析

时间复杂度：遍历一次数组，时间复杂度为O(N)

空间复杂度：O(N)

