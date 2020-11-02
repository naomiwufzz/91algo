# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
#
# 示例 1:
#
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 说明:
#
# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-distance-to-a-character

class Solution:
    def shortestToChar(self, S, C):
        # 复杂度O(N^2)
        distance = []
        target_index = []
        for i in range(len(S)):
            if S[i] == C:
                target_index.append(i)
        for i in range(len(S)):
            distance.append(min([abs(x - i) for x in target_index]))
        return distance




if __name__ == '__main__':
    sol = Solution()
    S = "loveleetcode"
    C = 'e'
    result = sol.shortestToChar(S, C)
    print(result)
