### 思路

#### 方法1：求和

计算应该有的和，减掉实际的和。差别就是缺失的数

#### 方法2：位运算

位运算：

~~~python
0 ^ 0 ^ 1 ^ 1 ... ^ k ^ (少个k) ^ n ^ n
~~~

缺失的相当于没有抵消掉，返回就是k

### 代码

~~~python
# 方法1：求和。数学的小技巧。
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        target_sum = (0 + n) * (n + 1) // 2
        result = target_sum - sum(nums)
        return result

# 方法2：位运算
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        res = n
        for i, num in enumerate(nums):
            res = res ^ i
            res = res ^ num
        return res
~~~

### 复杂度分析

- 时间复杂度：O(N)
- 空间复杂度：O(1)

