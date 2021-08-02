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

## 思路：KMP算法

没有太懂，还需要再看看

### 代码

~~~python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if not needle: return 0
        if m > n: return -1

        # 维护一个pattern的next数组
        def KMPNext(needle):
            next = [None] * len(needle)
            j = 0
            for i in range(1, len(needle)):
                while needle[i] != needle[j]:
                    if j > 0:
                        j = next[j - 1]
                    else:
                        next[i] = 0
                        break
                if needle[i] == needle[j]:
                    j += 1
                    next[i] = j
            return next

        next = KMPNext(needle)
        i, j = 0, 0

        while i < n and j < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1
            if j == m:
                return i - j

        return -1
~~~

### 复杂度分析

- 时间复杂度：O(m+n) 待匹配串和模式串长度和
- 空间复杂度：O(m)

