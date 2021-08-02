# 394. 字符串解码

~~~typora
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



### 思路

用栈辅助来判断左右括号拆出来的情况。为碰到`]`的时候可以全部进栈，需要注意，数字进栈的时候，要判断是否是连续的数字，如果是连续的，需要和前面的数字拼起来；碰到`[`的时候，用一个辅助的`temp_str`记录拼起来的字符串，这个`temp_str`在碰到数字的时候（其实就是碰到`[`）要乘数字的个数作为拼完的临时字符串。再判断此时栈是否还有`[`有的话说明临时字符串还要继续拼，把现有的临时串先入栈；如果`[`没有在栈中，可以拼到最终结果串中。全部结束，再判断一次栈是否为空，不空的话要拼进结果。这版写太长了，比较挫

### 代码

~~~python
class Solution:
    def decodeString(self, s: str) -> str:
        # 没碰到[的话全部进栈
        stack = []
        temp_str = ""
        result = ""
        for val in s:
            if val != ']':
                if stack:
                    if val.isdigit() and stack[-1].isdigit():  # 这里处理有可能多个数字的情况，比如100
                        stack[-1] = stack[-1] + val
                    else:
                        stack.append(val)
                else:
                    stack.append(val)
            else:
                while stack:  # 只要碰到]就出栈
                    item = stack[-1]
                    if item != '[' and not item.isdigit(): # 没碰到[和数字，先拼起来
                        stack.pop()
                        temp_str = item + temp_str
                    elif item == '[': # 碰到[不要拼
                        stack.pop()
                    elif item.isdigit(): # 碰到数字，要数字乘拼的内容
                        stack.pop()
                        temp_str = int(item) * temp_str
                        break #碰到数字就不要拼了
                if '[' not in stack:
                    while stack:
                        temp_str = stack.pop() + temp_str
                    result = result + temp_str
                    temp_str = ""
                else:
                    stack.append(temp_str)
                    temp_str = ""
        while stack:
            temp_str = stack.pop() + temp_str
        result = result + temp_str

        return result

~~~

### 复杂度分析

- 时间复杂度：O(N)，遍历一遍 
- 空间复杂度：O(N) 这里用到了一个最大长度为 `N` 的数组作为辅助空间stack，渐进空间复杂度为 O(N)

