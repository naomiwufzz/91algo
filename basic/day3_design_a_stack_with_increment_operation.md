### 思路

用数组模拟

方法比较朴素

### 代码

```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        # 如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
        if len(self.stack) < self.max_size:
            self.stack.append(x)

        else:
            pass

    def pop(self) -> int:
        # 弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1
        if len(self.stack) > 0:
            pop_value = self.stack[-1]
            self.stack = self.stack[:-1]
            return pop_value
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        # 栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(len(self.stack[:k])):
                self.stack[i] += val

```

### 复杂度分析

时间复杂度：初始化（构造函数）、`push` 操作和 `pop` 操作的渐进时间复杂度为 O(1)，`increment` 操作的渐进时间复杂度为 O(k)。

空间复杂度：O(N)

