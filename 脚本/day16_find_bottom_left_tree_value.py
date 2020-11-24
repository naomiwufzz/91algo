# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [] # 动态存储一层所有的节点，包括根节点、子节点、叶节点
        queue.append(root)
        while len(queue):
            curlevel = queue
            queue = [] # queue更新成一个空的
            for i in range(0, len(curlevel)):

                if curlevel[i].left:
                    queue.append(curlevel[i].left)
                if curlevel[i].right:
                    queue.append(curlevel[i].right)
        return curlevel[0].val
