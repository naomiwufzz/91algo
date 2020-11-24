# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        temp_node = dummy_head  # 直接从head开始会少一个
        while temp_node.next and temp_node.next.next:
            node_1 = temp_node.next
            node_2 = temp_node.next.next
            node_1.next = node_2.next
            node_2.next = node_1
            temp_node.next = node_2
            temp_node = temp_node.next.next  # 换完之后，移到next.next
        return dummy_head.next




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
result = Solution().swapPairs(head)
print(result.val)
print(result.next.val)
print(result.next.next.val)
print(result.next.next.next.val)
