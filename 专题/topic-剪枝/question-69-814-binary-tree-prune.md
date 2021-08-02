# 814.二叉树剪枝

~~~typora
给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

返回移除了所有不包含 1 的子树的原二叉树。

( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

示例1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1]
 
解释: 
只有红色节点满足条件“所有不包含 1 的子树”。
右图为返回的答案。


示例2:
输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]



示例3:
输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]



说明:

给定的二叉树最多有 200 个节点。
每个节点的值只会为 0 或 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-pruning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：递归+剪枝

用递归遍历树，递归出口是不是root。对于一个节点来说，先看左边，再看右边，如果该节点值是0，且左边和右边都没有节点，则剪枝（返回none）

### 代码

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right: # 没有左右节点，且值是0就剪掉
            root = None
        return root
        
~~~

### 复杂度分析

- 时间复杂度：O(n) ，n是节点个数（最坏可能全部剪掉）
- 空间复杂度：O(h)，h是树深度

