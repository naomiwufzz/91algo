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
