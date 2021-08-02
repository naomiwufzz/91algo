# 144.二叉树的前序遍历

~~~typora
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路1：递归

前序遍历就是根节点-左子节点-右子节点这样的顺序。

### 代码

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_lis = list()
        def preorder(root, node_lis):
            if not root:
                return node_lis
            node_lis.append(root.val)
            preorder(root.left, node_lis)
            preorder(root.right, node_lis)
            return node_lis
        return preorder(root, node_lis)
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量。每一个节点被遍历一次
- 空间复杂度：O(n) 递归的空间复杂度要考虑递归过程中栈的开销，平均情况下为O(logn)，最坏情况下，树是链状的，为O(n)

## 思路2：迭代

迭代的方式可以实现递归的，其实是一样的，只是递归的时候隐式维护了一个栈，而迭代的时候显示模拟了这个栈。

### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_lis = list()
        node_stack = list()
        if not root:
            return node_lis
        root_node = root
        while node_stack or root_node:
            while root_node:
                node_lis.append(root_node.val)
                node_stack.append(root_node)
                root_node = root_node.left
            root_node = node_stack.pop()
            root_node = root_node.right
        return node_lis


```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量，每个节点被遍历一次
- 空间复杂度：其中 O(n) 平均情况下栈的空间是O(logn)，最坏的情况树是链式的，就是O(n)

# 94.二叉树的中序遍历

```typora
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

## 题目解读



## 思路1：递归

前序遍历就是左子节点-根节点-右子节点这样的顺序。

### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []
        def inorder(root, node_list):
            if not root: # 递归出口
                return node_list
            inorder(root.left, node_list)
            node_list.append(root.val)
            inorder(root.right, node_list)
            return node_list
        return inorder(root, node_list)
```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量。每一个节点被遍历一次
- 空间复杂度：O(n) 递归的空间复杂度要考虑递归过程中栈的开销，平均情况下为O(logn)，最坏情况下，树是链状的，为O(n)

## 思路2：迭代

迭代的方式可以实现递归的，其实是一样的，只是递归的时候隐式维护了一个栈，而迭代的时候显示模拟了这个栈。

### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []
        if not root:
            return node_list
        node_stack = []
        node_root = root
        while node_stack or node_root:
            while node_root:
                node_stack.append(node_root)
                node_root = node_root.left
            node_root = node_stack.pop()
            node_list.append(node_root.val)
            node_root = node_root.right
        return node_list
```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量，每个节点被遍历一次
- 空间复杂度：其中 O(n) 平均情况下栈的空间是O(logn)，最坏的情况树是链式的，就是O(n)

# 145.二叉树的后序遍历

```typora
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

## 题目解读



## 思路1：递归

后序遍历就是左子节点-右子节点-根节点这样的顺序。

### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []
        def post_order(root, node_list):
            if not root:
                return node_list
            post_order(root.left, node_list)
            post_order(root.right, node_list)
            node_list.append(root.val)
            return node_list
        return post_order(root, node_list)
```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量。每一个节点被遍历一次
- 空间复杂度：O(n) 递归的空间复杂度要考虑递归过程中栈的开销，平均情况下为O(logn)，最坏情况下，树是链状的，为O(n)

## 思路2：迭代

后序遍历的思路稍微复杂一些，以下代码，似懂非懂。

### 代码

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        node_list = []
        if not root:
            return node_list
        node_stack = []
        node_root = root
        while node_stack or node_root:
            while node_root:
                node_stack.append(node_root) # 节点入栈
                # 后续遍历可能会碰到node的左已经空了但右还有一个节点，这个时候右边这个节点也是要先被遍历到的
                # 先遍历到底
                if node_root.left:
                    node_root = node_root.left # 节点更新为左节点
                else:
                    node_root = node_root.right
            # 节点空了的时候。
            node_root = node_stack.pop()
            node_list.append(node_root.val)
            # 找下一个root走的地方：如果弹出的节点是左节点，就去找右子树，
            # 如果弹出的是右节点，说明已经到最后的右节点了。node_root更新为none,继续进入while循环，弹出节点
            if node_stack:
                if node_root == node_stack[-1].left:
                    node_root = node_stack[-1].right
                else:
                    node_root = None
            # 栈空了的情况,要更新node_root为空，不然pop不出来了
            else:
                node_root = None

        return node_list

```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量，每个节点被遍历一次
- 空间复杂度：其中 O(n) 平均情况下栈的空间是O(logn)，最坏的情况树是链式的，就是O(n)