# def is_same_dic(target_dic, sub_dic):
#     for item in target_dic:
from collections import defaultdict
import collections

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


# class Solution(object):
#     def findSubstring(self, s, words):
#         dic_words = collections.Counter(words)
#         word_len = len(words[0])
#         window_len = word_len * len(words)
#         res = []
#         for i in range(len(s) - word_len + 1):
#             dic_cur = defaultdict(int)
#             for j in range(i, i + window_len, word_len):
#                 if s[j: j + word_len] not in dic_words:
#                     break
#                 if s[j: j + word_len] not in dic_cur:
#                     dic_cur[s[j: j + word_len]] = 1
#                 else:
#                     dic_cur[s[j: j + word_len]] += 1
#
#             if dic_cur == dic_words:
#                 res.append(i)
#
#         return res

s = "barfoothefoobarman"
words = ["foo","bar"]

print(Solution().findSubstring(s, words))
