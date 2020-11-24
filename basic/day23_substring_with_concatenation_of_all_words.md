### 思路

由于目标的words中的单词可能是重复的，因此可以用hash存储词和出现的次数，对比目标hash和子串hash是否一致，若一致，子串就是需要的结果。

### 代码

~~~python
class Solution:
    def findSubstring(self, s, words):
        # 获取words的哈希表1;顺便获取目标字符串长度
        word_length = len(words[0])
        target_length = word_length * len(words)
        target_dic = {}
        for item in words:
            if item not in target_dic:
                target_dic[item] = 1
            else:
                target_dic[item] += 1
        result_list = []

        if len(s) - target_length < 0:
            return result_list
        else:
            for i in range(len(s) - target_length+1):
                substring = s[i:(i+target_length)] # 符合条件的子串，子串长度是确定的
                substring_dic = {}
                idx1 = 0
                while idx1 < target_length:
                    idx2 = idx1+word_length
                    sub_word = substring[idx1:idx2]
                    if sub_word in words:
                        if sub_word in substring_dic:
                            substring_dic[sub_word] += 1
                        else:
                            substring_dic[sub_word] = 1
                        idx1 += word_length
                    else: break

                if substring_dic == target_dic:
                    result_list.append(i)
        return result_list
~~~

### 复杂度分析

- 时间复杂度：O(n * m)，`n` 为 s 的长度，`m` 为 words 中单词个数。
- 空间复杂度：O(m)，`m` 为 words 中单词个数。

