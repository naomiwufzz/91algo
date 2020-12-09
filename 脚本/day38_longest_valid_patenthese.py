# 一开始的思路是用栈放进去左括号，用一个变量在右括号匹配成功的时候+2（还觉得想到能够匹配的一定是双数非常机智）
# 但是碰到"()(()"问题，就卡住了。
# 全都是()其实没必要记住括号，记住位置就可以
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # 只记录位置就可以，因为每次都是append左括号
            elif s[i] == ')':
                if not stack:  # 栈是空的说明前面的匹配完了
                    stack.append(i)
                else:
                    top = stack.pop()
                    result = i - stack[-1]
                    max_result = max(max_result, result)
        return max_result

print(Solution().longestValidParentheses("((()()))"))