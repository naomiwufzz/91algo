class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        left = 0
        right = length-1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
        return left


nums = [1, 3, 5, 6]
target = 7
print(Solution().searchInsert(nums, target))