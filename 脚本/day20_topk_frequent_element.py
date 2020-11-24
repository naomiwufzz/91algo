class Solution:
    def topKFrequent(self, nums, k: int):
        if len(nums) < 1:
            return None
        freq ={}
        for i in range(len(nums)):
            value = nums[i]
            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1
        top_values = []

        top = sorted(freq.values(), reverse=True)[:k]
        for key, v in freq.items():
            if v in top:
                top_values.append(key)
        return top_values

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))