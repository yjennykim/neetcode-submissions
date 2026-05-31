from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]  # Use list comprehension to create a fresh board
        
        def is_valid(row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True

        def dfs(row):
            if row == n:  # All queens are placed
                res.append([''.join(r) for r in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = 'Q'  # Place queen
                    dfs(row + 1)  # Move to next row
                    board[row][col] = '.'  # Backtrack

        res = []
        dfs(0)
        return res
