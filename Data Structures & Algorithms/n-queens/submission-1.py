from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        
        def is_valid(row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            return True
        
        def dfs(row, col):
            if row == n:  # All queens are placed
                res.append([''.join(r) for r in board])
                return
            
            if col >= n:  # Move to the next row if all columns in the current row are explored
                return
            
            if is_valid(row, col):
                board[row][col] = 'Q'  # Place queen
                dfs(row + 1, 0)  # Move to the next row, start from column 0
                board[row][col] = '.'  # Backtrack
            
            # Explore the next column in the same row
            dfs(row, col + 1)

        dfs(0, 0)  # Start with the first row and first column
        return res
