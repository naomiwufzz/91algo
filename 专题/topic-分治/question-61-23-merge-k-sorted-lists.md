# 23.合并k个链表

~~~typora
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：分治

考虑两个链表排序，是较为容易的情况。用分治的思想，把`k`个链表拆成一对一对，再两两合并回来。

### 代码

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)

        #  单独判断基础的case
        if length == 0: return None
        if length == 1: return lists[0] # 已经升序，直接返回
        if length == 2: return self.mergeTwoLists(lists[0], lists[1])

        mid = length // 2

        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))
    
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
        # 考虑两个链表的排序
        res = ListNode(0) # 一个dummy头
        c1, c2, c3 = l1, l2, res
        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    c3.next = ListNode(c1.val)
                    c1 = c1.next
                else:
                    c3.next = ListNode(c2.val)
                    c2 = c2.next
                c3 = c3.next
            elif c1:
                c3.next = c1
                break
            elif c2:
                c3.next = c2
                break
        return res.next
~~~

### 复杂度分析

- 时间复杂度：O(knlogk)  
- 空间复杂度：O(logk) 

