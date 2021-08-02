# 28.实现strStr()

https://leetcode-cn.com/problems/implement-strstr

## 题目描述

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

~~~

## 题目解读

这个是典型的字符串单模式匹配问题。常见的字符串匹配算法包括暴力匹配、Knuth-Morris-Pratt 算法、Boyer-Moore 算法、Sunday 算法等

## 方法1：滑动窗口+子串逐一比较（暴力匹配）

### 思路

用一个`needle`的长度的窗口滑动一遍`haystack`，如果窗口内和`needle`一样，直接可以输出

### 代码

~~~python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # 需要注意haystack为空的时候不是直接输出0的，是-1
            return 0
        if len(haystack) >= len(needle):
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:(i+len(needle))] == needle:
                    return i
        return -1
~~~

### 复杂度分析

时间复杂度：`O((m-n)*n)=O(m*n)？？`要看最坏的情况下的复杂度

空间复杂度：`O(1)`并不会因为n的变化导致分配的空间有变化。只需要常数量级的空间保存一些变量

看算法执行的临时空间是否随变量n的变化而变化

## 方法2：Knuth-Morris-Pratt算法

KMP可以从前面的O(m*n)减少到O(m+n)，因为kmp减少了重复匹配的消耗。kmp算法本身目的就是从原字符串中找到匹配的字符串

