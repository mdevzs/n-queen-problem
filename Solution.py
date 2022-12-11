class Solution:

    def solveNQueens(self, n):
        board = [["."] * n for _ in range(n)]
        result = []

        self.dfs(n, board, result, 0)
        return result

    def dfs(self, n, board, result, row):
        if row == n:
            result.append(["".join(ele) for ele in board[:]])

        for col in range(n):
            if self.isValid(n, board, row, col):
                board[row][col] = "Q"
                self.dfs(n, board, result, row + 1)
                board[row][col] = "."

    def isValid(self, n, board, row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False

        newRow = row - 1
        j = 1
        while newRow >= 0:
            if col - j >= 0:
                if board[newRow][col - j] == "Q":
                    return False
            if col + j < n:
                if board[newRow][col + j] == "Q":
                    return False
            newRow -= 1
            j += 1

        return True
