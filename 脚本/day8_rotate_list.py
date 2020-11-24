class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
            n += 1  # n保存链表长度
        circle.next = head

        new_circle_tail = head
        rotate_time = n - (k % n) - 1  # 转动的次数
        for i in range(rotate_time):
            new_circle_tail = new_circle_tail.next
        new_circle_head = new_circle_tail.next
        new_circle_tail.next = None
        return new_circle_head


l = ListNode(1)
l.next = 2
l.next = 3
l.next = 4
l.next = 5
print(l.val)
