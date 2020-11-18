### 思路

先bfs获得所有的节点和对应的坐标，再对坐标进行排序

### 代码

~~~python
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
~~~

### 复杂度分析

时间复杂度：O(N)

空间复杂度：O(N)

