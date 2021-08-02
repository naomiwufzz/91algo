# **1456.定长子串中元音的最大数目**

~~~typora
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。

 

示例 1：

输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
示例 5：

输入：s = "tryhard", k = 4
输出：1
 

提示：

1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：滑动窗口

比较常规和简单的滑动窗口

### 代码

~~~python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left = 0
        right = 0
        count, max_count = 0, 0
        while right <= len(s)-1:
            if right <= k-1:
                if s[right] in vowels:
                    count += 1
            else:
                if s[right] in vowels:
                    count += 1
                if s[left] in vowels:
                    count -= 1
                left += 1
            right += 1
            max_count = max(count, max_count) # 放在后面，因为可能s很小以至于窗口不用移动左边
        return max_count    

~~~

### 复杂度分析

- 时间复杂度：O(n) 
- 空间复杂度：O(1)

