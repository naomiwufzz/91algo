### 思路

用栈存储括号对。遇到右括号就出栈并检查是否匹配

### 代码

~~~python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'(':')','{':'}','[':']'}
        for paren in s:
            if paren in valid:
                stack.append(paren)
            else:
                if not stack: return False  # 可能有stack是空的情况，就无法pop操作
                valid_left = stack.pop()
                if valid[valid_left] != paren:
                    return False
        if not stack:  # 循环结束的时候，stack应该是空的，非空可能是"["
            return True
        else:
            return False


~~~

### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度：O(n)

