import collections


class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        count_letter = collections.Counter(letters)  # 生成一个计数字典,记录letters里面的字母各有多少
        scores = []  # 记录所有单词的分数
        for word in words:
            each = 0
            for c in word:
                each += score[ord(c) - ord('a')]  # 距离a的距离
            scores.append(each)

        res = [0]

        def dfs(start, cur_score):
            if cur_score > res[0]:
                res[0] = cur_score  # 目前的分大于res[0]存储目前的分

            for i in range(start, len(words)):
                valid = True
                for c in words[i]:  # 对于word里面每一个字母
                    count_letter[c] -= 1  # 计数减掉1
                    if c not in count_letter or count_letter[c] < 0: # 没这个字母或者没有这个字母可以减了说明不valid
                        valid = False
                if valid:
                    dfs(i + 1, cur_score + scores[i])
                for c in words[i]:
                    count_letter[c] += 1  # 再加回去
            return res[0]

        return dfs(0, 0)