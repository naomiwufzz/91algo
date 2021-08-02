# 208.实现Trie（前缀树）

~~~typora
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：利用辅助的结构化Trienode

定义一个`TrieNode`，子节点全部放在字典当中（英文的话子节点最多26个），插入、查找都是从`root`开始，一个个往下看，子节点是否包含某个字符

### 代码

~~~python
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化根节点
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for cha in word:
            if cha not in node.children: # 不存cha子节点的话新建一个
                node.children[cha] = TrieNode() 
            node = node.children[cha]
        node.is_end = True # 除了最后一个子节点，前面的就默认False即可

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for cha in word:
            if cha not in node.children:
                return False
            node = node.children[cha]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for cha in prefix:
            if cha not in node.children:
                return False
            node = node.children[cha]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
~~~

### 复杂度分析

- 时间复杂度：插入查找都是O(len(word))  
- 空间复杂度：最坏的情况，没有共同前缀，全部都要占位存储，前缀树高度是m，字母表大小是n的话，最坏是O(m*n)

