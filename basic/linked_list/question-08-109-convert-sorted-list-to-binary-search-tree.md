# 107.有序链表转换二叉搜索树

~~~typora
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



### 思路

利用快慢指针，找到最中间的node作为一个根节点，根节点左边的用于构造左子树，右边的用于构造右子树。用递归的方式构造完整的树。（快慢指针会了，递归树和平衡二叉树还没完全理解）

### 代码

~~~python
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
        if not head:
            return head
        pre_node_of_slow = None  # 要记录slow的前一个位置
        slow = head
        fast = head
        while fast and fast.next:  # 这个循环结束的时候slow是中点
            fast = fast.next.next
            pre_node_of_slow = slow
            slow = slow.next
        if pre_node_of_slow:
            pre_node_of_slow.next = None

        node = TreeNode(val=slow.val)
        if fast == slow:
            return node

        node.left = self.sortedListToBST(head=head)
        node.right = self.sortedListToBST(head=slow.next)
        return node

~~~

### 复杂度分析

- 时间复杂度：O(logn) 递归树的深度是logn，每层的操作是n
- 空间复杂度：O(logn) 

