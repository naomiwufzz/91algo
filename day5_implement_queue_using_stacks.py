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

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
q.pop()

