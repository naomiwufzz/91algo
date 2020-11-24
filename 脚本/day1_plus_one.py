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

class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10 # % 表示取余数， //表示取商 carry是1触发下一位继续计算

        return [carry] + digits if carry else digits # 这个是如果最后为0，在最前面加1,carry是1的时候在前面加1，否则直接输出
    # 但是这个算法会强制所有的N遍历一遍，原来的方法其实[1, 2, 3]只到最后一位就输出了
    # 这个解法了解一下就可以了。感觉并没有特别好，其中的计算比较精妙，但算法没有必要记

if __name__ == '__main__':
    sol = Solution()
    inputs = [[1, 2, 3], [1, 2, 9], [9, 9, 9], [0], [1, 9, 8], [1, 9], [9]]
    for input in inputs:
        result = sol.plusOne(input)
        print(result)