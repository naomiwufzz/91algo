## 144.二叉树前序遍历

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
        res = []
        def dfs(root):
            if not root:
                return None
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
~~~

## 145.二叉树后序遍历

### 代码

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
```

## 94.二叉树中序遍历

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
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
```

## 102.二叉树层序遍历

### 代码

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        node_que = [root]
        res = []
        while node_que:
            level = []
            for _ in range(len(node_que)):
                node = node_que.pop(0)
                level.append(node.val)
                if node.left:
                    node_que.append(node.left)
                if node.right:
                    node_que.append(node.right)
            res.append(level)
        return res
```

### 

