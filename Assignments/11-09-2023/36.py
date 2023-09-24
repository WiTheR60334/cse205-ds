class Solution(object):
    def isValidSudoku(self, board):
        ans = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    ans += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(ans) == len(set(ans))