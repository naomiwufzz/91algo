# 129. 求根节点到叶节点数字之和

~~~typora
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

 

示例 1：


输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
示例 2：


输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
 

提示：

树中节点的数目在范围 [1, 1000] 内
0 <= Node.val <= 9
树的深度不超过 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

二叉树路径题目是非常重要的题型

## 思路1：深度优先DFS+递归

每个节点的求和值，是左子树和右子树的和。递归出口是碰到叶子节点的子节点，也就是节点为空

### 代码

~~~python
# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, pre_sum: int) -> int:
            if not root:  # 递归出口
                return 0
            pre_sum = pre_sum * 10 + root.val
            if not root.left and not root.right:  # 说明是路径最后面，也就是碰到了叶子节点。叶子节点不需要加左右子节点结果
                return pre_sum
            else: # 说明是根节点，对每个根节点，要加左右子节点结果
                return dfs(root.left, pre_sum) + dfs(root.right, pre_sum)
        return dfs(root, 0)
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：O(h) h是树的深度

## 思路2：广度优先BFS（即层序遍历）

维护两个队列，第一个队列用来存放node，第二个队列用来存放到这个node的时候计算的值。层序遍历，就是第一层先入队，弹出第一层根节点，找到左右子节点入队列，再依次出队列，就是一层层节点遍历了。只有碰到子节点的时候才需要sum添加值，中间过程都不需要

### 代码

```python
# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum = 0 # 初始化和
        node_queue = [root]
        value_queue = [root.val]
        while node_queue:
            node = node_queue.pop(0)
            val = value_queue.pop(0)
            left_node, right_node = node.left, node.right
            if not left_node and not right_node: # 说明是叶子节点
                sum += val
            else:
                if left_node:
                    value_queue.append(val*10 + left_node.val)
                    node_queue.append(left_node)
                if right_node:
                    value_queue.append(val*10 + right_node.val)
                    node_queue.append(right_node)
        return sum
```

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：其中 O(Q) 需要维护节点队列。最坏的情况是n
