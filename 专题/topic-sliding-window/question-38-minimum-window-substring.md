# **76.最小覆盖子串**

~~~typora
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：哈希+滑动窗口

乍看一下好像跟昨天差不多，怎么就是hard了。其实很大的区别在于，窗口的大小这次不是固定的。右指针移动的条件是，不超过s，左指针的移动条件是window_dict在元素数量上覆盖target_dict（注意不是等于），只要覆盖就满足题目条件

### 代码

~~~python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = collections.defaultdict(int)
        # 对t构建目标哈希
        for val in t:
            target_dict[val] += 1
        min_length, min_start = float('inf'), 0
        # 初始化滑动窗口
        left, right = 0, 0
        # 记录滑动窗口中出现的目标字符
        valid = 0  # 记录window_dict是否包含target_dict
        window_dict = collections.defaultdict(int)
        while right < len(s):

            if s[right] in target_dict:
                window_dict[s[right]] += 1
                if window_dict[s[right]] == target_dict[s[right]]:
                    valid += 1
                while valid == len(target_dict):
                    if right - left < min_length:
                        min_start = left
                        min_length = right - left
                    if s[left] in target_dict:
                        if window_dict[s[left]] == target_dict[s[left]]:
                            valid -= 1
                        window_dict[s[left]] -= 1
                    left += 1
            right += 1
        return s[min_start:(min_start+min_length+1)] if min_length < float('inf') else ''


~~~

### 复杂度分析

- 时间复杂度：O(N + K)O(N+K)，N 为 S 串长度，K 为 T 串长度
- 空间复杂度：O(S)，其中 S 为 T 字符集元素个数

