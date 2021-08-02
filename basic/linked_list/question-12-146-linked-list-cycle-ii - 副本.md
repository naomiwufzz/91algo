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



## 思路：哈希表+双向链表

没有完全理解，似懂非懂，根据官方题解，加了自己的理解改写的。尽力加了自己理解的注释。



### 代码

~~~python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # 存储最大容量
        # 两个数据结构，一个双向链表，一个哈希表
        # 生成一个双向链表, 同时保存该链表的头结点与尾节点
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        # 把头尾连起来生成初始的双向链表
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 # 为什么要一个size
        # 生成存储值的哈希表
        self.cache = dict()

    def get(self, key: int) -> int:
        # 如果哈希表中不存在该值，不用考虑
        if key not in self.cache:
            return -1
        else:

        # 如果哈希表中存在该值, 获取改值，并移动到头部
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # key 不在哈希表的情况
            node = DoubleLinkedNode()
            # node 添加到哈希表
            self.cache[key] = node
            # node 放进双向链表头部
            self.add_to_head(node)
            self.size += 1
            # 判断是否要删除
            if self.size > self.capacity:
                # 超出了容量，需要删掉双向链表的尾部节点
                removed_node = self.remove_tail()
                self.cache.pop(removed_node.key)
                self.size -= 1
        else:
            # key 在哈希表中的情况，需要修改value，并移动到头部
            node = self.cache[key]
            node.value = value # 更新
            self.remove_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

~~~

### 复杂度分析

- 时间复杂度：O(1) 遍历两遍
- 空间复杂度：O(capacity) 



