## 206.反转链表

### 代码

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
~~~

## 92.反转链表ii

### 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            """反转以head为开头的链表"""
            pre = None
            cur = head
            while cur:
                next_cur = cur.next
                cur.next = pre
                pre = cur
                cur = next_cur
        # 虚拟头节点，用于消除复杂的分类讨论
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        # pre走到left节点前一个结点
        for _ in range(left-1): 
            pre = pre.next
        left_node = pre.next
        right_node = pre
        # rightnode 走到要反转的节点
        for _ in range(right-left+1):
            right_node = right_node.next
        cur = right_node.next
        # 切出来要截取的链表
        pre.next = None
        right_node.next = None
        reverse_linked_list(left_node)
        # 接回原来的链表
        pre.next = right_node
        left_node.next = cur
        return dummy_node.next
```

## 25. k个一组反转链表

### 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, head, tail):
            """反转head到tail段的链表"""
            prev = tail.next
            cur = head
            while prev != tail: # 要以prev为结束点
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return head, tail
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        while head:
            tail = pre
            # 剩余部分如果没有k个的话就不反转了
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy_node.next
            # k个一组反转
            head, tail = self.reverse_linked_list(head, tail)
            pre.next = tail
            pre = head
            head = head.next    
        return dummy_node.next
```

