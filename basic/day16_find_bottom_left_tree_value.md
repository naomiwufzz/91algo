### 思路

用层序遍历BFS，动态存储每一层自左向右的节点，最后一层第一个就是需要的结果

### 代码

~~~python
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

~~~

### 复杂度分析

时间复杂度：O(N)

空间复杂度：O(N)

