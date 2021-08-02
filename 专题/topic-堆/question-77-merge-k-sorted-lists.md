# 23.合并k个升序链表

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
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：堆

先入堆，再拿出来（后续可以考虑是不是建堆的时候只放根节点快？）

### 代码

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        head = []
        for i in range(len(lists)): # 遍历的是listnode，不是数组
            if lists[i]: # 说明不为空
                while lists[i]:
                    heapq.heappush(head, lists[i].val) # (lists[i].val, i)的元组
                    lists[i] = lists[i].next
        while head:
            val = heapq.heappop(head)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
            
~~~

### 复杂度分析

- 时间复杂度：O(n\*k\*logn) 
- 空间复杂度：O(n) 

