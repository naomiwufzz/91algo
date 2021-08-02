# 98. 验证二叉搜索树

~~~typora
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

**BST 的中序遍历是升序序列**这个性质很重要

## 思路1：中序遍历（DFS）

中序遍历的数组是升序的话那么就是`bst`。直接数组进行对比。第一个写法是根据中序的模板写的，比较模式化，不灵活。就是把中序遍历的值都存储到数列中，最后检查这个数列是否是严格的升序数列。写法2是不借助列表，直接递归返回的就是`bool`，递归来说更优雅一些。时间空间复杂度没有区别

### 代码

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 写法1
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True # 提交的时候写的False也过了
        
        def dfs(root, node_lis):
            if not root:
                return node_lis
            dfs(root.left, node_lis)
            node_lis.append(root.val)
            dfs(root.right, node_lis)
            return node_lis
        node_lis = dfs(root, [])
        for i in range(len(node_lis)-1): # 要注意直接sort是不行的，因为右节点要大于左节点，等于也不可以
            if node_lis[i] >= node_lis[i+1]:
                return False
        return True

# 写法2
class Solution:
    def isValidBST(self, root: TreeNode, pre_val=float("-inf")) -> bool:
        if not root:
            return True
        is_bst_left = self.isValidBST(root.left, pre_val)
        if root.val > pre_val:
            pre_val = root.val
            is_bst = True
        else:
            is_bst = False
        is_bst_right = self.isValidBST(root.right,pre_val)
        return is_bst and is_bst_left and is_bst_right
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量。遍历了整个树
- 空间复杂度：O(n) 用了长度为n的数组存储了中序序列

## 思路2：定义法

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

  