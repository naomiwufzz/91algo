### 思路

加1有两种情况：

1.该数位不为9，直接加1

2.该数位为9，加1之后，该位置变成0，并且前一个位置加1。特别的，如果是99...99全是9的情况，需要在最前面insert一个1加一个位数

所以可以倒序遍历一次数组，从个位数开始，**如果不是9，就直接加1，如果是9就变成0之后，移到下一数位**，一直重复，直到遍历到位置0

有两个要注意的情况：

1.array长度为1的情况：这种情况会导致range的遍历无法开始，`range(0,0,-1)`是没有输出的，所以要遍历到-1。注意range是左闭右开的。我一开始就是因为没到-1导致了array length是1的时候没有输出

2.99....99全是9的情况：可以在最后的时候检查，我一开始在中间检查，导致代码较为冗余

其实逻辑就是从后往前遍历，非9就加1直接结束，是9就改成0继续遍历。最后加一个全是0的情况的补充

### 代码

~~~python
class Solution:
    def plusOne(self, digits):
        array_length = len(digits)

        for i in range(array_length-1, -1, -1): # 注意range是左闭右开，end为-1才会遍历到0
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits.insert(0,1)
        return digits


if __name__ == '__main__':
    sol = Solution()
    inputs = [[1, 2, 3], [1, 2, 9], [9, 9, 9], [0], [1, 9, 8], [1, 9], [9]]
    for input in inputs:
        result = sol.plusOne(input)
        print(result)
~~~

### 复杂度分析

时间复杂度：遍历一次数组，时间复杂度为O(N)

空间复杂度：O(1)

