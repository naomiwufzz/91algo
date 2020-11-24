class MyQueue1:

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
        elif len(self.stack2) != 0:  # 第一次写的时候这里有问题,没加这个判断，直接全部倒入右栈。其实如果右栈不为空的时候，没必要从左栈倒入
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



q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.pop()
q.push(5)
print(q.peek())
q.pop()

