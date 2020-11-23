class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        dic = {}
        i = 0
        max_length = 0
        while i < len(s):
            if s[i] not in dic:  # 当元素不在哈希表中的时候，放入哈希表，并记住位置
                dic[s[i]] = i
                i += 1
            else:
                if len(dic) > max_length:
                    max_length = len(dic)
                idx = dic[s[i]] # 找到该重复元素的位置，并删掉重复位子之前的所有元素，重新计算长度
                del_val = []

                for index, v in dic.items():
                    if v <= idx:
                        del_val.append(index)
                for val in del_val: del dic[val]
                dic[s[i]] = i
                i += 1
        if len(dic) > max_length:
            max_length = len(dic)
        return max_length


#  双指针

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len


s = "abcab"
print(Solution().lengthOfLongestSubstring(s))
