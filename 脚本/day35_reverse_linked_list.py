# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针的方法，思路会清楚一点
        pre = None
        post = head
        while post:
            tmp = post.next
            post.next = pre
            pre = post
            post = tmp
        return pre


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        head_result = head
        # 先找到m的位置
        i = 1  # i在第一个head
        while i < m:
            prev = head  # prev记录开始反转的链表部分前一个节点
            head = head.next # head是开始反转的部分
            i += 1
        if m == 1:
            prev = head
            head = head
        pre = None
        current = head  # 从current.next开始反转

        j = n-m
        while j <= n:
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
            j += 1
        prev.next = pre
        head.next = current
        return head_result


