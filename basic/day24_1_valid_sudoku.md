### 思路

**方法：一次迭代**

一个简单的解决方案是遍历该 `9 x 9` 数独 **三** 次，以确保：

- 行中没有重复的数字。
- 列中没有重复的数字。
- `3 x 3` 子数独内没有重复的数字。

### 代码

~~~python
class Solution:
    def isValidSudoku(self, board):
        # 9个rows，9个columns，9个boxes
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9): # row i
            for j in range(9): # column j
                value = board[i][j]
                print(i, rows[i])
                if value != '.':
                    if value not in rows[i]:
                        rows[i][value] = 1
                    else:
                        return False
                    if value not in columns[j]:
                        columns[j][value] = 1
                    else:
                        return False

                    box_index = (i // 3) * 3 + j // 3
                    if value not in boxes[box_index]:
                        boxes[box_index][value] = 1
                    else:
                        return False
        return True
~~~

### 复杂度分析

- 时间复杂度：O(1) 只需要81个格子遍历一遍
- 空间复杂度：O(1)

