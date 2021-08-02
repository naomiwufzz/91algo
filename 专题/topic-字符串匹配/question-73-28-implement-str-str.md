# 28.实现strstr()函数

~~~typora
实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 

示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0
 

提示：

0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读

## 思路：RK算法

这好像是以前的题。可以用复杂的字符串匹配方法解决。RK算法也用的滑窗，区别是，原来的滑窗是直接匹配字符串，这个滑窗是比较哈希值。这个哈希值用一个哈希映射（这里用的是26进制）

### 代码

~~~python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 一些特殊情况
        if not haystack and not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        if not needle:
            return 0
        # 初始化
        hash_val = 0 # haystack的哈希值默认为0
        target = 0 # 目标hash。即needle的hash
        # 用26进制的hash编码
        for i in range(len(haystack)):
            if i < len(needle):
                hash_val = hash_val * 26 + (ord(haystack[i]) - ord("a"))
                target = target * 26 + (ord(needle[i]) - ord("a"))
            else:
                hash_val = (
                    hash_val - (ord(haystack[i - len(needle)]) - ord("a")) * 26 ** (len(needle) - 1)
                ) * 26 + (ord(haystack[i]) - ord("a"))
            if i >= len(needle) - 1 and hash_val == target:
                return i - len(needle) + 1
        return 0 if hash_val == target else -1
~~~

### 复杂度分析

- 时间复杂度：O(m+n) 待匹配串和模式串长度和
- 空间复杂度：O(1)

