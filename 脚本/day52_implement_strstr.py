# bf方法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if needle[0] == haystack[i]:  # 相当于触发
                flag = True
                for j in range(len(needle)):
                    if not needle[j] == haystack[i + j]:
                        flag = False
                if flag:
                    return i
        return -1





haystack = "hello"
needle = "ll"
result = Solution().strStr(haystack, needle)
print(result)