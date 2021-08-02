# 513. 找树左下角的值

~~~typora
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

二叉树路径题目是非常重要的题型

## 思路1：广度优先（层序遍历）

题目说最后一层的最左，层序遍历是很自然想到的

### 代码

~~~python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 层序遍历
        node_lis = [[root.val]]
        cur_nodes = []
        prev_nodes = [root]
        while prev_nodes:
            node = prev_nodes.pop(0)  # 出队列
            if node.left:
                cur_nodes.append(node.left)
            if node.right:
                cur_nodes.append(node.right)
            if not prev_nodes:
                prev_nodes = cur_nodes
                node_lis.append([node.val for node in cur_nodes])
        return node_lis[-1][0]

# 学习官方题解
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:

            result = queue[0].val
            for _ in range(len(queue)):  # 这里有一个改进是循环queue的长度的话就不用纠结current_cur_lis 和prev_cur_lis
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：O(Q) Q是队列长度，最坏的情况是满二叉树，此时和n同阶

## 思路2：DFS

前序和中序和后续遍历都可以。树的最后一行最左边，就是前序/中序遍历到的最后一行的第一个出现的左子节点，因为前序和中序遍历一定是左子节点最先处理

### 代码

```python
# 前序
class Solution:
    def __init__(self):
        self.res = 0
        self.max_level = 0

    def findBottomLeftValue(self, root: TreeNode) -> int:

        def dfs(root, level):  # 前序遍历就是左子节点，root，右子节点的顺序。要记录一个层数。层数一上升就更新最新层左子节点的值
            if not root:
                return None
            # 处理root。层级比最大层级大的第一个就可以记录
            if level > self.max_level:
                self.max_level = level
                self.res = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            return self.res

        return dfs(root, 0)
# 中序
class Solution:
    def __init__(self):
        self.res = 0
        self.max_level = 0
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.res = root.val # 要注意中序和后续要先处理一下res。不然h为1的树，如[1]不会进入后面的递归
        def dfs(root, level): # 前序遍历就是左子节点，root，右子节点的顺序。要记录一个层数。层数一上升就更新最新层左子节点的值
            if not root:
                return None
            # 处理root
            
            dfs(root.left, level+1)
            if level > self.max_level:
                self.max_level = level
                self.res = root.val 
            dfs(root.right, level+1)
            
            return self.res
        
        return dfs(root, 0)
# 后序
class Solution:
    def __init__(self):
        self.res = 0
        self.max_level = 0
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.res = root.val
        def dfs(root, level): # 前序遍历就是左子节点，root，右子节点的顺序。要记录一个层数。层数一上升就更新最新层左子节点的值
            if not root:
                return None
            # 处理root
            
            dfs(root.left, level+1)
            
            dfs(root.right, level+1)
            if level > self.max_level:
                self.max_level = level
                self.res = root.val 
            return self.res
        
        return dfs(root, 0)
```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：其中 O(h) h是树的高度
