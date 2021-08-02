# 464.我能赢吗

~~~typora
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-i-win
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
~~~

## 题目解读



## 思路：dp

没有太懂。

理解的部分：首先通过排除一些特殊情况直接返回，相当于减枝，使计算量小一些。递归树的逻辑是，一个分支到底，对方有一种方式赢不了我就赢了。用位运算是为了序列化set，是一种优化方式，也可以不用

### 代码

~~~python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 特殊情况
        if desiredTotal > maxChoosableInteger:
            return True
        if sum(maxChoosableInteger+1) < desiredTotal:
            return False
        def dp(picked, acc): # acc是累计的数值
            if acc >= desiredTotal:
                return False
            if picked == (1 << (maxChoosableInteger + 1)) - 1:
                return False
            for n in range(1, maxChoosableInteger):
                if picked & 1 << n == 0:
                    if not dp(picked | 1<<n, acc+n):
                        return True
            return False
        return dp(0, 0)


        
~~~

### 复杂度分析

- 时间复杂度：O(2^maxChoosableInteger) 
- 空间复杂度：O(2^maxChoosableInteger)

