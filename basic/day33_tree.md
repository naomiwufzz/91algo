### 思路

前中后序遍历都用递归（迭代的方法后续补）；层序遍历用一个queue维护每一层的nodes，遍历完该层把该层清空逐个放入该层nodes的左右节点

### 代码

#### 前序遍历

~~~python
class Solution:
    def __init__(self):
        self.lis = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        self.lis.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.lis


~~~

#### 中序遍历

~~~python
class Solution:
    def __init__(self):
        self.lis = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return

        self.inorderTraversal(root.left)
        self.lis.append(root.val)
        self.inorderTraversal(root.right)

        return self.lis

~~~

#### 后续遍历

~~~python
class Solution:
    def __init__(self):
        self.lis = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.lis.append(root.val)
        return self.lis

~~~



#### 层序遍历

~~~python
class Solution:
    def levelOrder(self, root: TreeNode):
        node_lists = []
        queue = []
        queue.append(root)
        while queue:
            current_level = queue
            queue = []
            node_list =[]
            for i in range(len(current_level)):
                if current_level[i]: # current_level[i] 也可能是空的
                    node_list.append(current_level[i].val)
                    if current_level[i].left:
                        queue.append(current_level[i].left)
                    if current_level[i].right:
                        queue.append(current_level[i].right)
            if node_list: # 空的情况按题目要求的不要的
                node_lists.append(node_list)
        return node_lists
~~~



### 复杂度分析

- 时间复杂度：都为O(N)
- 空间复杂度：递归都为O(h) h是树的深度

