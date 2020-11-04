# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        sub_str = ''

        for element in s:

            if element != ']': # 如果不是]就压入栈
                stack.append(element)
            elif element == ']': # 如果碰到]，出栈整个字符串
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                if stack[-1] == '[':
                    stack.pop() # 把[push出栈
                    num = 0
                    digit = 1
                    while len(stack) > 0: # 注意要考虑数字不止一位数的情况
                        if stack[-1].isdigit():
                            num += int(stack.pop()) * digit
                            digit *= 10
                        else:
                            break
                    sub_str = num * sub_str
                    stack.append(sub_str) # 出来之后整个字符串重新进栈
                    sub_str = ''

        result_str = ''.join(stack)
        return result_str



sol = Solution()
result = sol.decodeString("s10[bc]")
print(result)