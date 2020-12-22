### 思路

BF暴力方法

### 代码

~~~python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)-len(needle)+1): # 这个range是为了保证haystack字符串的i:能够包含neddle字符串
            if needle[0] == haystack[i]:  # 相当于触发
                flag = True
                for j in range(len(needle)):
                    if not needle[j] == haystack[i + j]:
                        flag = False
                if flag:
                    return i
        return -1
~~~

### 复杂度分析

- 时间复杂度：O(N*M)
- 空间复杂度：O(1)

