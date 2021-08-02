# 677.键值映射

~~~typora
实现一个 MapSum 类，支持两个方法，insert 和 sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
 

示例：

输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

提示：

1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/map-sum-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路1：前缀树

用一个`count_val`属性记录节点是结尾的情况，有几个这个单词。搜索前缀的时候，到前缀结尾的时候用dfs找到所有的`count_val`

### 代码

~~~python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count_val = 0 # count表示以该节点为前缀的字符的个数

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.trie
        for cha in key:
            if cha not in curr.children:
                curr.children[cha] = TrieNode()
            curr = curr.children[cha]
        curr.count_val = val

    def sum(self, prefix: str) -> int:
        curr = self.trie
        for cha in prefix:
            if cha not in curr.children:
                return 0
            curr = curr.children[cha]

        res = 0
        def dfs(curr_node): # dfs找到curr_node之后所有有count的节点并加和
            nonlocal res
            if curr_node.count_val != 0:
                res += curr_node.count_val
            for c in curr_node.children:
                dfs(curr_node.children[c])
        dfs(curr)
        return res
            

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
~~~

### 复杂度分析

- 时间复杂度：O(len(key))，key 是待插入的字串
- 空间复杂度：插入操作是线性复杂度O(n)  ，sum 操作最坏情况是O(m^n)

## 思路2：hashmap

用一个`count_val`属性记录节点是结尾的情况，有几个这个单词。搜索前缀的时候，到前缀结尾的时候用dfs找到所有的`count_val`

### 代码

```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key] = val

    def sum(self, prefix: str) -> int:
        count = 0
        for k in self.hashmap:
            if k.startswith(prefix):
                count += self.hashmap[k]
        return count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

### 复杂度分析

- 时间复杂度：O(N) N是不重复的key的个数
- 空间复杂度：插入操作是线性复杂度O(1)  ，sum 操作是O(n*s)s是前缀长度

