# **438.找到字符串中所有字母的异位词**

~~~typora
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：哈希+滑动窗口

一个哈希表存储`p`的信息，一个哈希表动态存储滑动窗口中和`p`对应的信息。相等的时候，结果中添加左指针

### 代码

~~~python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_table = {}
        hash_sliding = {}
        res = []
        for i in range(len(p)):
            if p[i] not in hash_table:
                hash_table[p[i]] = 1
                hash_sliding[p[i]] = 0
            else:
                hash_table[p[i]] += 1
        left, right = 0, 0
        while right < len(s):
            if right < len(p):
                if s[right] in hash_table:
                    hash_sliding[s[right]] += 1
            else:
                if s[right] in hash_table:
                    hash_sliding[s[right]] += 1
                if s[left] in hash_table:
                    hash_sliding[s[left]] -= 1
                left += 1
            right += 1
            if hash_sliding == hash_table:
                res.append(left)
        return res
~~~

### 复杂度分析

- 时间复杂度：O(n)  n为s长度
- 空间复杂度：O(1) 因为哈希表不会超过26个字母 

