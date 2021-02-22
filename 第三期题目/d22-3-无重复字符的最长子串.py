class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        word_hash = {} # 用一个hash存储字母的位置
        max_length = 0
        for i in range(len(s)):
            if s[i] not in s[left:right]:  # 新碰到的字母不在滑动窗口框定里面
                word_hash[s[i]] = i
                right += 1  # 右边的指针向右移动
                max_length = max(max_length, right - left)
            else:  # 重复的时候
                max_length = max(max_length, right - left)
                left = word_hash[s[i]] + 1
                word_hash[s[i]] = i
                right += 1

        return max_length