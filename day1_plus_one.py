class Solution:
    def plusOne(self, digits):
        array_length = len(digits)
        if array_length == 1:
            if digits[0] < 9:
                digits[0] += 1
            else:
                digits[0] = 0
                digits.insert(0,1)
            return digits
        for i in range(array_length-1, 0, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            else:
                digits[i] = 0
                if digits[i-1] < 9:
                    digits[i-1] += 1
                    return digits
                else:
                    if i-1 == 0 and digits[i-1] == 9:
                        digits[0] = 0
                        digits.insert(0, 1)
                        return digits
                    else:
                        continue

if __name__ == '__main__':
    sol = Solution()
    inputs = [[1, 2, 3], [1, 2, 9], [9, 9, 9], [0]]
    for input in inputs:
        result = sol.plusOne(input)
        print(result)