from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = defaultdict(set) # index: set of numbers
        valid_cols = defaultdict(set)
        valid_grids = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                value = board[r][c]
                if value == '.':
                    continue
                
                grid_key = (r//3, c//3)
                if value in valid_rows[r] or value in valid_cols[c] or value in valid_grids[grid_key]:
                    return False
                
                valid_rows[r].add(value)
                valid_cols[c].add(value)
                valid_grids[grid_key].add(value)
        
        return True