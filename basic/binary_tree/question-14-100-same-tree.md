# 100.相同的树

~~~typora
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false
 

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路1：深度优先DFS+递归

树的问题要从最小的子问题入手，最小的问题是树高度为1的时候。判断两个树是否相同，就是判断结点值相同+左子树相同+右子树相同。递归出口是，p或者q为空的情况，

### 代码

~~~python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val: # 这个条件不一定写在出口中。可以是p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：O(h) h是树的深度

## 思路2：广度优先BFS（即层序遍历）

先遍历树的第一层，一个个node比较，再遍历树的第二层，一个个node比较，用队列保存节点（先进先出，越早的节点是越上层的节点）

### 代码

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        queue1 = [p]
        queue2 = [q]
        while queue1 and queue2:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if not left1 or not left2:
                if left1 or left2:
                    return False  # left1 left2都为空的情况不能直接continue，不然下面的会无法计算

            if not right1 or not right2:
                if right1 or right2:
                    return False
            if left1:  # 要考虑有可能为空的情况。如果空的进入队列，就无法找到val
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2 # 全部搜索完成，两个队列都是空的时候，说明两个树是一样的

```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：其中 O(Q) Q 为队列的长度最大值，在这里不会超过相邻两层的节点数的最大值。

## 思路3：前序和中序遍历判断是否为同一个树

单前中后序无法确定一颗树，需要中序+前或者后遍历可以确定是同一棵树

### 代码

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrder(node, arr):
            if not node:
                arr.append(None)
                return arr
            arr.append(node.val)
            preOrder(node.left, arr)
            preOrder(node.right, arr)
            return arr

        def inOrder(node, arr):
            if not node:
                arr.append(None)
                return arr
            inOrder(node.left, arr)
            arr.append(node.val)
            inOrder(node.right, arr)
            return arr
        return preOrder(p, []) == preOrder(q, []) and inOrder(p, []) == inOrder(q, [])
```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：其中 O(n) 遍历的时候需要数组保存节点，最多保存n个节点