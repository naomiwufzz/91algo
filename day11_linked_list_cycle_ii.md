### 思路

比较直接的哈希法

保存见到过的ListNode判断ListNode是不是重复，如果是的话，就是有环，且为环的开始

### 代码

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hash = set()
        while head:
            if head in hash:
                return head
            else:
                hash.add(head)
                head = head.next
        return None
```

### 复杂度分析

时间复杂度：遍历一次数组，时间复杂度为O(N)

空间复杂度：O(1)

