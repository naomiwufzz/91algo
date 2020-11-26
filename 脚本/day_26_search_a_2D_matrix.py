# 直接拉长成一个一维列表，用二分查找法

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)  # 行数
        if m < 1:
            return False
        n = len(matrix[0])  # 列数 总长度应该是 m * n
        left = 0
        right = m * n - 1

        while left <= right:  # 注意这里不可以是!=,会导致无法退出
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            elif mid_value > target:
                right = mid - 1
        return False





matrix =  [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 6
print(Solution().searchMatrix(matrix, target))
