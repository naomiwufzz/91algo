# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode):

        seen = []
        def dfs(node, x=0, y=0):
            if node:
                seen.append([x, y, node.val])
                dfs(node.left, x-1, y-1)
                dfs(node.right, x+1, y-1)
        dfs(root)
        seen = sorted(seen, key=lambda x: (x[0], -x[1], x[2]))
        result_lis = []
        vertical = [seen[0][2]]
        for i in range(1, len(seen)):
            if seen[i][0] == seen[i-1][0]:
                vertical.append(seen[i][2])
            else:
                result_lis.append(vertical)
                vertical = []
                vertical.append(seen[i][2])
        result_lis.append(vertical)
        return result_lis

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = sol.verticalTraversal(root)
print(result)