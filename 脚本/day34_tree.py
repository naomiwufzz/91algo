# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.lis = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        self.lis.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.lis

class Solution:
    def __init__(self):
        self.lis = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return

        self.inorderTraversal(root.left)
        self.lis.append(root.val)
        self.inorderTraversal(root.right)

        return self.lis
class Solution:
    def __init__(self):
        self.lis = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.lis.append(root.val)
        return self.lis

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
                if current_level[i]:
                    node_list.append(current_level[i].val)
                    if current_level[i].left:
                        queue.append(current_level[i].left)
                    if current_level[i].right:
                        queue.append(current_level[i].right)
            if node_list:
                node_lists.append(node_list)
        return node_lists
