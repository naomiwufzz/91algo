# 513. 找树左下角的值

~~~typora
297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例 1：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：

输入：root = [1,2]
输出：[1,2]
 
~~~

## 题目解读

## 思路1：广度优先（层序遍历）

序列化就是直接的广度优先，反序列化需要注意root走一步，左右子节点走两步，如果碰到null，则node跳过，左右子节点不用走。实际操作当中，要注意需要一个队列来维护tree_node，（一开始写treenode是独立的没有连起来）在这个队列中，是node的情况要入队，不是node的情况直接跳过就行了

### 代码

~~~python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ''
        if not root:
            return '[null]'
        prev = [root]
        while prev:
            node = prev.pop(0)
            if node:
                res = res + str(node.val) + ','  # 按题目要求还有逗号
                prev.append(node.left)
                prev.append(node.right)
            else:
                res += 'null,'
        res = '['+res[:-1]+']'
        print(res)
        return res  # 去掉最后逗号

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if data == 'null':
            return None
        data = data.split(',')
        root = TreeNode(data[0])
        # 如果单根据i找node的话，会导致node独立，不形成一个tree
        # 一个queue保存TreeNode，一个data决定node的值
        queue = [root]
        i = 0
        while i < len(data)-2:

            node = queue.pop(0)
            # l和r指针，在data列中每次都走两步
            # l和r形成node的放进
            l_node_val = data[i+1]
            r_node_val = data[i+2]
            if l_node_val != 'null':
                l_node = TreeNode(l_node_val)
                node.left = l_node
                queue.append(l_node)
            if r_node_val != 'null':
                r_node = TreeNode(r_node_val)
                node.right = r_node
                queue.append(r_node)
            i += 2
        return root
~~~

### 复杂度分析

- 时间复杂度：O(n) n为树节点数量
- 空间复杂度：O(Q) Q是队列长度，最坏的情况是满二叉树，此时和n同阶

