class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                result = mid  # 因为是向下取，所以在这里要存储result
                left = mid + 1
            else:
                right = mid - 1
        return result

result = Solution().mySqrt(4)
print(result)