# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         hash = {}
#         while head.next:

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 定义哈希集合
        hash = set()
        # 遍历链表
        while head:
            # 判断是否存在于集合中
            # 存在返回当前节点
            if head in hash:
                return head
            # 不存在则将节点放入集合中，继续遍历
            else:
                hash.add(head)
                head = head.next
        # 链表无环，返回 None
        return None


y = ListNode(3)
y.next = None
x = ListNode(4)
x.next = y

sol = Solution()
sol.detectCycle(y)

