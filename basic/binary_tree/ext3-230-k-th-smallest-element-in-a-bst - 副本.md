# 230. 二叉搜索树中第K小的元素

~~~typora
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

 

示例 1：


输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：


输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
 

 

提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

**BST 的中序遍历是升序序列**这个性质很重要

## 思路1：中序遍历获得有序序列（DFS）

对于`bfs`，也就是`Binary Search Tree`有一个很重要的性质，中序遍历能够获得有序的数列（从小到大）。取第`k-1`个数就可以

### 代码

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def inorder(root, node_lis):
            if not root:
                return node_lis
            inorder(root.left, node_lis)
            node_lis.append(root.val)
            inorder(root.right, node_lis)
            return node_lis
        
        return inorder(root, [])[k-1]
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量。遍历了整个树
- 空间复杂度：O(n) 用了长度为n的数组存储了中序序列

## 思路2：中序遍历获得有序序列（迭代）

迭代的好处是，获得`k`个值之后就可以停止了，更快。就是中序遍历迭代版本的一个小优化。需要多练习

### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        node_stack = [] # 辅助栈
        node_lis = []
        node_stack.append(root)
        node = root 
        while node_stack or node:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            node_lis.append(node.val)
            if len(node_lis) == k:
                return node_lis[-1]
            node = node.right     
                
```

### 复杂度分析

- 时间复杂度：O(H+k) H是树的高度，当树是一个平衡树时：复杂度为 O(logN+k)。当树是一个不平衡树时：复杂度为 O(N+k)，此时所有的节点都在左子树。

- 空间复杂度：O(H+k)。当树是一个平衡树时：O(logN+k)。当树是一个非平衡树时：O(N+k)。

  