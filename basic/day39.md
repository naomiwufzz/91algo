### [剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

难度简单147

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 `appendTail` 和 `deleteHead` ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，`deleteHead` 操作返回 -1 )

 

**示例 1：**

```
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```

**示例 2：**

```
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```

**提示：**

- `1 <= values <= 10000`
- `最多会对 appendTail、deleteHead 进行 10000 次调用`

### 思路

用两个栈倒来倒去。一个栈用于存储输入，一个栈用于弹出最先进入的数字。在输入之前把右边的都倒入左边，在左边进栈，在删除元素的时候，把左边的全部倒入右边弹出

### 代码

~~~python
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        self.stack1.append(value)


    def deleteHead(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else: return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
~~~

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(n)

### [641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)

难度中等65

设计实现双端队列。
你的实现需要支持以下操作：

- MyCircularDeque(k)：构造函数,双端队列的大小为k。
- insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
- insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
- deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
- deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
- getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
- getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
- isEmpty()：检查双端队列是否为空。
- isFull()：检查双端队列是否满了。

**示例：**

```
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4
 
```

 

**提示：**

- 所有值的范围为 [1, 1000]
- 操作次数的范围为 [1, 1000]
- 请不要使用内置的双端队列库。

### 思路

用数组实现

### 代码

```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = []
        self.max_length = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) < self.max_length:
            self.deque.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) < self.max_length:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.deque:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.deque:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.deque:
            return False
        else:
            return True

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.deque) == self.max_length:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()




```

### 复杂度分析

- 时间复杂度：O(1)
- 空间复杂度：O(k)