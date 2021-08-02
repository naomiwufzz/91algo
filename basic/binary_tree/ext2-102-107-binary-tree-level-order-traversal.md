# 102.二叉树的层序遍历

~~~typora
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：层序遍历BFS

层序遍历用队列维护node

### 代码

~~~python
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
        node_queue = []
        cur_level_queue = [root]
        node_queue.append([root.val])
        upper_level_queue = cur_level_queue
        while upper_level_queue:
            cur_level_queue = []
            for i in range(len(upper_level_queue)):
                if upper_level_queue[i].left:
                    cur_level_queue.append(upper_level_queue[i].left)
                if upper_level_queue[i].right:
                    cur_level_queue.append(upper_level_queue[i].right)
            if cur_level_queue:
                node_queue.append([node.val for node in cur_level_queue])
            upper_level_queue = cur_level_queue
        return node_queue

~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：O(n) 队列中最多存n个节点

