# 面试题17.17. 多次搜索

~~~typora
给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

示例：

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
提示：

0 <= len(big) <= 1000
0 <= len(smalls[i]) <= 1000
smalls的总字符数不会超过 100000。
你可以认为smalls中没有重复字符串。
所有出现的字符均为英文小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multi-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：前缀树

把`smalls`做成前缀树，对`big`每个字母为开头的字符串进行查找

### 代码

~~~python
import collections
class Trie:
    def __init__(self, words):
        self.trie = {}
        for word in words: # 直接全部insert进去
            curr_node = self.trie
            for cha in word:
                if cha not in curr_node:
                    curr_node[cha] = {}
                curr_node = curr_node[cha]
            curr_node['end'] = word
        
    def search(self, word):
        res = [] # 可能匹配到多个前缀，直接都返回
        curr_node = self.trie
        for cha in word:
            if cha not in curr_node:
                break # 这里直接结束查找即可
            curr_node = curr_node[cha]
            if 'end' in curr_node:
                res.append(curr_node['end'])
        return res

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie(smalls)
        matched_smalls = collections.defaultdict(list) # 默认list格式的字典
        for i in range(len(big)):
            matches = trie.search(big[i:])
            for small in matches:
                matched_smalls[small].append(i)
        res = []
        for small in smalls:
            res.append(matched_smalls[small])
        return res
~~~

### 复杂度分析

- 时间复杂度：O(n*k)，k是`smalls`中最长词长度，n是`big`长度
- 空间复杂度：O(s)  ，匹配成功的位置的数量

