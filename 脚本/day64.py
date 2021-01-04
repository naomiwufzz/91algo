# 暴力法
class Solution:
    def waysToSplit(self, nums) -> int:
        result = 0
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                left = nums[:i]
                mid = nums[i:j]
                right = nums[j:]
                if left and mid and right:
                    if sum(left) <= sum(mid) <= sum(right):
                        result += 1
        return result


class Solution:
    def waysToSplit(self, nums) -> int:
        mod = 10 ** 9 + 7  # 按题目要求结果要对mod取余
        n = len(nums)

        # 计算和保存前缀和
        pre_sum = [0] * n
        pre_sum[0] = nums[0]
        for i in range(n):
            pre_sum[i] = pre_sum[i-1] + nums[i]

        result = 0

        # 第一个切断点前缀和最大为sum(nums)/3
        first_cut_max = pre_sum[n-1] / 3
        for i in range(n):
            if pre_sum[i] > first_cut_max: break  # 第一个切断点的边界
            lower = self.lower_bound(i+1, n-1, pre_sum, 2 * pre_sum[i])
            upper = self.upper_bound(i+1, n-1, pre_sum, pre_sum[i]+(pre_sum[n-1] - pre_sum[i])/2)

            if upper >= lower:
                result += upper - lower + 1
        return result % mod


    @staticmethod
    def lower_bound(left, right, pre_sum, target):
        # 第二个断点的下边界
        # 在第一个断点到第二个断点之间找到满足sum(left) <= sum(mid)的情况。也就是pre_sum[result] <= 2 * pre_sum[first_cut]
        while left < right:
            mid = left + ((right - left) >> 1)
            if pre_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    @staticmethod
    def upper_bound(left, right, pre_sum, target):
        # 第二个断点的上边界
        # 在第一个断点和第二个断点之间找到满足sum(mid) = sum(mid+right)/2,pre_sum[result] = sum(mid+right)/2
        while left < right:
            mid = left + ((right - left) >> 1)
            if pre_sum[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left - 1



nums =[1,2,2,2,5,0]
result = Solution().waysToSplit(nums)
print(result)

