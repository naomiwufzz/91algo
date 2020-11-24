### 思路

卡了很久，一直弄不出`aa2[bvc]dd`的情况，会碰到`aa`和`dd`没有加入结果的情况。群里看了lucifer说的解答，我的节点就是，把substring找出来之后，要重新入栈，这个就很简洁

用栈来存储，遍历一遍，只要不是`]`就压入栈，如果是`]`开始一个个出栈字符串，直到碰到`[`。乘上之前的数字之后，再入栈。最后把栈中的元素加起来就是结果

注意：数字会有大于一位数的情况

### 代码

```python
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


```

### 复杂度分析

时间复杂度：遍历一次数组，时间复杂度为 O(N^2)。不确定。中间倒序取元素的时候是*N？

空间复杂度：O(N)。额外使用了栈的空间记录

