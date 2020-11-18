# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#  方法1：前序和中序遍历查看是否完全相同
def preorder(root,root_list):
    if not root:
        return root_list.append(None)
    root_list.append(root.val)
    preorder(root.left, root_list)
    preorder(root.right, root_list)
    return root_list
def inorder(root, root_list):
    if not root:
        return root_list.append(None)
    inorder(root.left, root_list)
    root_list.append(root.val)
    inorder(root.right, root_list)
    return root_list
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        preorder_p = preorder(p, [])
        inorder_p = inorder(p, [])
        preorder_q = preorder(q, [])
        inorder_q = inorder(q, [])
        if preorder_p == preorder_q and inorder_p == inorder_q:
            return True
        else:
            return False


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 不考虑左右的情况
        if not p and not q:  # pq都是空的话说明相等
            return True
        elif not p or not q:  # pq并非都是空，但是pq有一个是空说明肯定不相等
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


sol = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.right.left = TreeNode(6)
p.right.right = TreeNode(7)

print(preorder(p, []))
print(inorder(p, []))