# 1206.设计跳表

~~~typora
不使用任何库函数，设计一个跳表。

跳表是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 [30, 40, 50, 60, 70, 90]，然后增加 80、45 到跳表中，以下图的方式操作：


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

在本题中，你的设计应该要包含这些函数：

bool search(int target) : 返回target是否存在于跳表中。
void add(int num): 插入一个元素到跳表。
bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
了解更多 : https://en.wikipedia.org/wiki/Skip_list

注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

样例:

Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
约束条件:

0 <= num, target <= 20000
最多调用 50000 次 search, add, 以及 erase操作。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-skiplist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：跳表定义

先定义跳表节点，有向右和向下两个指针。

- 搜索：搜索比较简单，从上往下找，跳表节点和目标进行对比
- 添加：添加三个操作里面比较复杂的，添加需要一层层找，并且记录下来的路径，因为需要按0.5的概率把上层的跳表层填充上新的跳表节点。最后一层是肯定需要插入的，上面的层是按概率生成的
- 删除：删除和搜索差不多，区别是，删除的时候需要断掉该节点往后连即可

### 代码

~~~python
import random
class Node:
    """跳表节点"""
    def __init__(self, val=0):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:

    def __init__(self):
        # 初始化左右哨兵节点，因为num/target 的范围是0到20000，所以左右节点选择-1和20001
        # 选16层的原因:2^k >= 总数即可，k选16差不多6w多，是比5w多的
        left = [Node(-1) for n in range(16)]
        right = [Node(20001) for n in range(16)]
        for i in range(15): # 最后一层没有down了，所以只到15
            left[i].right = right[i]
            left[i].down = left[i+1]
            right[i].down = right[i+1]
        left[-1].right = right[-1]
        self.head = left[0]

    def search(self, target: int) -> bool:
        cur = self.head
        # 比较节点和目标值的大小，如果目标值比该节点右边大，那cur指针向右移，反之，向左移
        while cur:
            if cur.right.val > target:
                cur = cur.down
            elif cur.right.val < target:
                cur = cur.right
            else:
                return True
        return False

    def add(self, num: int) -> None:
        cur = self.head
        stack = [] # 要把往下走的路径都记录
        while cur:
            if cur.right.val >= num:
                stack.append(cur)
                cur = cur.down
            else:
                cur = cur.right
        pre = None
        while stack:
            cur = stack.pop()
            # 创建node并把node插入进去
            node = Node(num)
            node.right = cur.right
            cur.right = node
            if pre:
                node.down = pre
            pre = node
            if random.randint(0, 1): # 以1/2的概率从下往上生成新的跳表节点
                break

    def erase(self, num: int) -> bool:
        # 删除和查询比较类似，就是找到了需要重新连一下跳表节点
        cur = self.head
        is_removed = False
        while cur:
            if cur.right.val >= num:
                if cur.right.val == num:
                    is_removed = True
                    cur.right = cur.right.right
                cur = cur.down
            elif cur.right.val < num:
                cur = cur.right
        return is_removed



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
~~~

### 复杂度分析

- 时间复杂度：O(log(n)) 查询、插入、删除均是
- 空间复杂度：O(n) 

