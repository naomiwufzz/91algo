### [1052. 爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner/)

难度中等49收藏分享切换为英文接收动态反馈

今天，书店老板有一家店打算试营业 `customers.length` 分钟。每分钟都有一些顾客（`customers[i]`）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 `i` 分钟生气，那么 `grumpy[i] = 1`，否则 `grumpy[i] = 0`。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 `X` 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 

**示例：**

```
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
```

**提示：**

- `1 <= X <= customers.length == grumpy.length <= 20000`
- `0 <= customers[i] <= 1000`
- `0 <= grumpy[i] <= 1`



### 思路

#### 方法1：滑动窗口

最直接的想法是从0位置开始0~X不生气，计算满意的数量，1~X+1计算满意的数量，以此类推。如果每次都重新算复杂度会很高。考虑每次滑动窗口的时候，减掉退出窗口的数，加上进入窗口的数

### 代码

~~~python
# 思路1代码
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        # 先计算总共满意的数量
        satisfy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfy += customers[i]
        if len(customers) < X:
            return satisfy
        # 计算窗口在0位置的时候的满意的数量
        for i in range(X):
            if grumpy[i] == 1:
                satisfy += customers[i]
        max_satisfy = satisfy
        for i in range(1, len(customers) - X + 1):
            if grumpy[i-1] == 1:
                satisfy -= customers[i-1]
            if grumpy[i+X-1] == 1:
                satisfy += customers[i+X-1]
            if satisfy > max_satisfy:
                max_satisfy = satisfy
        return max_satisfy
~~~

### 复杂度分析

- 时间复杂度：遍历的叠加 O(N)
- 空间复杂度：O(1)

