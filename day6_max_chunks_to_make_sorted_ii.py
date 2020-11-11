# hint: Each k for which some permutation of arr[:k] is equal to sorted(arr)[:k] is where we should cut each chunk.
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        i = 0
        sorted_arr = sorted(arr)
        cut_time = 1
        while i < len(arr):
            if arr[:i] == sorted_arr[i]:
                cut_time += 1
                i += 1
                continue
            else:
                sub_arr = arr[i:i+2]  # 截取这个arr,如果能cut成功，最大的chunk不超过2
                if sorted(sub_arr) == sorted_arr[i:i+2]:
                    cut_time += 1
                    i += 1
                else:
                    i += 1
        return cut_time

sol = Solution()
result = sol.maxChunksToSorted([5,4,3,2,1])
print(result)
result = sol.maxChunksToSorted([2,1,3,4,4])
print(result)


