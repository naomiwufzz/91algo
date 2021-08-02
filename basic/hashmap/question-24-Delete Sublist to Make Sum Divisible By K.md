# Delete sublist to make sum divisible by k

~~~typora
You are given a list of positive integers nums and a positive integer k. Return the length of the shortest sublist (can be empty sublist ) you can delete such that the resulting list's sum is divisible by k. You cannot delete the entire list. If it's not possible, return -1.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 8, 6, 4, 5]
k = 7
Output
2
Explanation
We can remove the sublist [6, 4] to get [1, 8, 5] which sums to 14 and is divisible by 7.
~~~

## 题目解读



## 思路：哈希方法+同余定理

根据题解的推导可以得出代码思路。用一个哈希表存储前缀和取余的结果，key为前缀和对k取的余数，value为位置。只要判断前缀和减掉target对k取余是否在哈希表中即可。要注意0的情况需要额外考虑。

### 代码

~~~python
def delete_min_sublis(nums, k):
    target = sum(nums) % k
    hash_map = {0: -1}
    pre_sum = 0
    res = len(nums)
    for i in range(len(nums)):
        pre_sum += nums[i]
        modulus = pre_sum % k
        hash_map[modulus] = i
        if (pre_sum-target) % k in hash_map:
            res = min(res, i-hash_map[(pre_sum-target) % k])
    return -1 if res == len(nums) else res

res = delete_min_sublis([1, 8, 6, 4, 5], 7)
print(res)
~~~

### 复杂度分析

- 时间复杂度：O(n) 一层循环
- 空间复杂度：O(n) 用了哈希表


