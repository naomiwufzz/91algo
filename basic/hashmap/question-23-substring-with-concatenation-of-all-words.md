# 3.无重复字符的最长字串

~~~typora
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：哈希方法+双指针结合

循环地找长度跟目标长度一样的子串，然后在这个子串当中看是否子子串都在目标哈希表中

### 代码

~~~python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hash_map = dict()  #
        max_length = 0
        left_pointer, right_pointer = 0, 0
        for right_pointer in range(len(s)):
            # 说明在左右指针中间的字符串中无重复。右指针指的点不在hash中or右指针指的点虽然在hash中，但是不在左右指针包含的串中
            if s[right_pointer] not in hash_map or hash_map[s[right_pointer]] < left_pointer:
                hash_map[s[right_pointer]] = right_pointer
                if right_pointer - left_pointer + 1 >= max_length:
                    max_length = right_pointer - left_pointer + 1
            else:  # 说明左右指针当中重复了
                if right_pointer - left_pointer >= max_length:
                    max_length = right_pointer - left_pointer
                left_pointer = hash_map[s[right_pointer]] + 1
                hash_map[s[right_pointer]] = right_pointer
        return max_length
~~~

### 复杂度分析

- 时间复杂度：O(n^2) 两层循环
- 空间复杂度：O(m), m 为 words 数组元素个数


