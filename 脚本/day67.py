# 双指针，滑动窗口
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        alpha = {'a', 'e', 'i', 'o', 'u'}
        left, right = 0, 0
        num_alpha = 0
        while right < k:  # 先把窗口右边移到k的地方，并记录元音数量
            if s[right] in alpha:
                num_alpha += 1
            right += 1
        max_alpha = num_alpha
        while k <= right < len(s):
            if s[right] in alpha:
                num_alpha += 1
            if s[left] in alpha:
                num_alpha -= 1
            max_alpha = max(num_alpha, max_alpha)
            right += 1
            left += 1

        return max_alpha
result = Solution().maxVowels("rhythms", 4)
print(result)