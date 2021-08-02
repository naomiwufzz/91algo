# 974.和可被k整除的子数组

~~~typora
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：哈希表+前缀和+同余定理

子串的问题要联想前缀和的使用

### 代码

~~~python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0  # 初始化前缀和
        mod_dic = {0:1}  # 0 需要特殊考虑。如果是0，直接从-1位开始取也是答案
        for val in nums:
            pre_sum += val
            modulus = pre_sum % k
            if modulus in mod_dic:
                mod_dic[modulus] += 1
            else:
                mod_dic[modulus] = 1
        res = 0
        for i, v in mod_dic.items():
            res += v * (v-1) / 2
        return int(res)

~~~

### 复杂度分析

- 时间复杂度：O(n) 遍历一遍
- 空间复杂度：O(n) 用一个哈希表记录值，是O(n) 


