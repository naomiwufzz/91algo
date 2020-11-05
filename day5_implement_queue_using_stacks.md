题目：https://leetcode-cn.com/problems/implement-queue-using-stacks/ 

### 思路

思路1：暴力实现：用两个栈互相倒，入队列时候把右栈全倒出来进左栈之后入新的数字，出队列的时候把左栈全部倒入右栈。peak的时候如果右栈不为空说明所有的数字都已经倒入右栈了，否则把左栈的数全部倒入右栈再取最后一个。

思路2：左右栈都进行数据存储。入队列push的时候，全部都入左栈。出队列的时候，如果右栈不是空的，最上面的一定是最先进入队列的数字，如果右栈是空的就麻烦一点，所以要用一个数值（我的是`self.peak_value`）来记录左栈栈底元素

### 代码

```python
# 思路1
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = [] # stack 只能push、pop、peak和length
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)
        print(self.stack1)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) + len(self.stack2) == 0:
            return True
        else:
            return False

# 思路2
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []  # stack 只能push、pop、peak和length
        self.stack2 = []
        self.peek_value = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.stack1) == 0:
            self.peak_value = x  # 左栈空的时候，需要记录栈底的元素
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        elif len(self.stack2) != 0:  # 第一次写的时候这里有问题。其实如果右栈不为空的时候，没必要从左栈倒入
            pass
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:

            return self.peak_value

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) + len(self.stack2) == 0:
            return True
        else:
            return False
```

### 复杂度分析

**思路1时间复杂度：**

push：最好O(1)，最坏O(N)

pop：O(N)。或者可以倒完再倒回左栈，这样左栈就是O(1）pop是O(N)不变

peak：最好O(1) 最坏O(N)

empty：O(1)

**思路1空间复杂度**：O(N)。N为队列的大小

**思路2时间复杂度：**

push：O(1)

pop：O(N)

peak：O(1) 

empty：O(1)

**思路1空间复杂度**：O(N)。N为队列的大小

