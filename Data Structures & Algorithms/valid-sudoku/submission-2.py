class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = {} # index: set of numbers
        valid_cols = {}
        valid_grids = {} 

        for r in range(len(board)):
            for c in range(len(board[r])):
                value = board[r][c]
                if value == '.':
                    continue

                if r not in valid_rows:
                    valid_rows[r] = set()
                if c not in valid_cols:
                    valid_cols[c] = set()
                grid_key = (r//3, c//3)
                if grid_key not in valid_grids:
                    valid_grids[grid_key] = set()
                
                if value in valid_rows[r] or value in valid_cols[c] or value in valid_grids[grid_key]:
                    return False
                
                valid_rows[r].add(value)
                valid_cols[c].add(value)
                valid_grids[grid_key].add(value)
        
        return True