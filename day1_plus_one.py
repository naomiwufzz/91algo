class Solution:
    def plusOne(self, digits):
        array_length = len(digits)

        for i in range(array_length-1, -1, -1): # -1的时候把数组长度为1的情况和别的情况合并，每种情况都不会遍历到-1
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i-1 != -1 and digits[i-1] < 9: # 对i-1是-1的情况进行拦截
                    digits[i-1] += 1
                    return digits
                else:
                    continue
        if digits[0] == 0:
            digits.insert(0,1)
        return digits


if __name__ == '__main__':
    sol = Solution()
    inputs = [[1, 2, 3], [1, 2, 9], [9, 9, 9], [0], [1, 9, 8], [1, 9], [9]]
    for input in inputs:
        result = sol.plusOne(input)
        print(result)
