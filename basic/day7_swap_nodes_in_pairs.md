### 思路

画图，把要换的链表换一下指针，注意的是，需要开头有一个dummy_head，不然的话交换完会找不到head

### 代码

~~~python
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


~~~

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(n)

