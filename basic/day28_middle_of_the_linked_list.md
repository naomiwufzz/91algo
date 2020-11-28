### 题目描述

给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

```
示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 

提示：

给定链表的结点数介于 1 和 100 之间。
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 思路

一个快指针，一个慢指针，快指针每次走两步，满指针每次走一步，这样就保证快指针是慢指针速度的两倍。如果快指针能走两步就走两步，不能走两步的时候但能走一步的时候，就是双数listnode的情况，那慢指针继续走一步（因为题目要求双数的情况取后面那个数）

### 代码

~~~python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next

        return slow
~~~

### 复杂度分析

- 时间复杂度：O(N)
- 空间复杂度：O(1)

