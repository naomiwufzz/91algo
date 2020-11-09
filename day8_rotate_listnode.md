### 思路

把链表先闭合成环，再找到head往右移动k的地方解开环

注意：会有None和node只有1的情况

### 代码

```python
class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not head:
            return None
        if not head.next:
            return head

        circle = head
        n = 1
        while circle.next:
            circle = circle.next
            n += 1
        circle.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head
```

### 复杂度分析

时间复杂度：分别遍历两次链表，时间复杂度为 O(N)。

空间复杂度：O(1)

