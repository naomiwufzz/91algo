# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def find_median(left_node, right_node):
            # 找链表的中间node。用左右指针的方法.
            # 注意，未必是整个链表的中点，要泛化为任何两个node的中点
            fast = left_node
            slow = left_node
            while fast != right_node and fast.next != right_node:
                fast = fast.next.next
                slow = slow.next
            return slow
        def build_tree(left_node, right_node):
            if left_node == right_node:
                return None

            median = find_median(left_node, right_node)
            root = TreeNode(median.val)
            root.left = build_tree(left_node, median)
            root.right = build_tree(median, right_node)
            return root


        return build_tree(head, None)

