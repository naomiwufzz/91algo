# 24.两两交换链表中的节点

~~~typora
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



### 思路

需要一个dummy head作为开头的，不然开头的位置不好记录。

需要找到交换的最小单位进行循环迭代，本题最小单位是四个节点，`preNode -> A -> B -> tailNode`其中`preNode`可以是`dummy`也可以是链表中要交换的两个节点上面的那个节点，`tailNode`是下面一组要交换的家电的开始，也可以是`None`。找到最小的单位，只需要注意最小单位里面需要交换三个链表指针。交换完就需要找下一个最小单位，我们需要两个记录指针记录`node`的位置，只需要`preNode`和`curNode`即可。需要注意的是，本题要直接改变原来的链表的，修改节点本身。

![1621255247385](C:\Users\naomi\AppData\Roaming\Typora\typora-user-images\1621255247385.png)



### 代码

~~~python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans = ListNode()
        ans.next = head  # 最前面放一个空的node
        pre_node = ans  # 初始化最开始的节点
        while head and head.next:
            # 定义一个变换单位的节点
            cur_node = head
            next_node = head.next
            next_cur_node = next_node.next
            # 对三个指针进行改动
            next_node.next = cur_node
            pre_node.next = next_node
            cur_node.next = next_cur_node
            # 移动pre和head到下一个最小单位
            pre_node = head
            head = next_cur_node

        return ans.next
~~~

### 复杂度分析

- 时间复杂度：O(N)，遍历一遍 
- 空间复杂度：O(1) 这里没用多余的内存空间

