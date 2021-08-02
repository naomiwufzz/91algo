# 160.相交链表

~~~typora
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路1：哈希方法

先遍历一遍A，把A节点都存入哈希表，再遍历一遍B，若节点已经在哈希表中，直接返回，若遍历完都不在哈希表中说明没有重合节点

### 代码

~~~python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_dic = dict()
        while headA:
            node_dic[headA] = 1
            headA = headA.next
        while headB:
            if headB in node_dic:
                return headB
            headB = headB.next
        return None
~~~

### 复杂度分析

- 时间复杂度：O(n) 遍历两遍
- 空间复杂度：O(n) 需要一个哈希表存储node 



## 思路2：双指针方法

把相交链表看作是三段，没有相交部分为两段`a,b`，相交部分为一段`c`。一个指针从a开始，走到结束再从b开头往后走，另一个指针从b开始，走到结束再从a开始往后走。两者相等的时候就是相交点。

为什么可以这样？从a开始的指针到交点走的路是`a+c+b`，从b开始的指针到交点走的路是`b+c+a`，路程一样的肯定会相交。

### 代码

```python
class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while a != b: # 如果a和b不相交的话，不会退不出循环，会在a、b都是None时退出
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next
        return a
```

### 复杂度分析

- 时间复杂度：O(n) 需要遍历
- 空间复杂度：O(1) 不需要额外的空间存储 

