class Solution:
    def isValidSudoku(self, board):
        # 9个rows，9个columns，9个boxes
        rows = [{} for i in range(9)] # 一开始用的是[{}]*9 这样会导致改动任何一个字典会改动所有字典的
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


input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().isValidSudoku(input))
