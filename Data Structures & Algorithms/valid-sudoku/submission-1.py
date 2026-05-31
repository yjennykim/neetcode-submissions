class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(len(board)):
            print("cols", cols.items())
            print("boxes", boxes.items())
            for c in range(len(board[0])):
                if board[r][c] == '.': 
                    continue
                    
                if r not in rows:
                    rows[r] = set()

                # check duplicates in rows
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if c not in cols:
                    cols[c] = set()

                # check duplicates in cols
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                
                if (r//3,c//3) not in boxes:
                    boxes[(r//3,c//3)] = set()
                
                # check duplicates in boxes
                if board[r][c] in boxes[(r//3,c//3)]:
                    return False

                boxes[(r//3,c//3)].add(board[r][c])

        return True

